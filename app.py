"""
News/IMDb Pro → Monday.com Opportunity Web App
Allows team members to paste a URL (news article or IMDb Pro) and automatically
create or update an opportunity in Monday.com's F & E Watchlist board.
"""
 
import os
import json
import re
import requests
from flask import Flask, render_template, request, jsonify
from anthropic import Anthropic
from dotenv import load_dotenv
 
load_dotenv()
 
app = Flask(__name__)
 
# ── Config ──────────────────────────────────────────────────────────────────
MONDAY_API_URL = "https://api.monday.com/v2"
MONDAY_API_TOKEN = os.getenv("MONDAY_API_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
 
WATCHLIST_BOARD_ID = 8888736546
DEAL_TRACKER_BOARD_ID = 8888736517
ACCOUNTS_BOARD_ID = 8888736490
SUBITEMS_BOARD_ID = 8900315469
JORDAN_SOLES_USER_ID = 20509600
 
# Column IDs for the Watchlist board
WATCHLIST_COLUMNS = {
    "description": "text_mkpvefv5",
    "accounts": "board_relation_mktba9wj",
    "stage": "color_mkpv8105",
    "production_status": "color_mkpvjyfe",
    "imdb_pro": "text_mkpvq4jn",
    "director": "board_relation_mktcr9tq",
    "type": "text_mkpv7jzp",
    "genre": "text_mkpv79wg",
}
 
PRODUCTION_STATUS_MAP = {
    "pre-production": "Pre-Prod",
    "in production": "Filming",
    "filming": "Filming",
    "post-production": "Post-Production",
    "released": "Released",
    "in development": "In Development",
    "announced": "Announced",
    "script": "Script",
    "on hold": "On Hold",
    "completed": "Completed",
    "rumored": "Rumored",
}
 
client = Anthropic(api_key=ANTHROPIC_API_KEY)
 
 
# ── Monday.com API helpers ──────────────────────────────────────────────────
 
def monday_query(query, variables=None):
    """Execute a Monday.com GraphQL query."""
    headers = {
        "Authorization": MONDAY_API_TOKEN,
        "Content-Type": "application/json",
        "API-Version": "2024-10",
    }
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    resp = requests.post(MONDAY_API_URL, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        raise Exception(f"Monday.com API error: {data['errors']}")
    return data
 
 
def search_board(board_id, search_term):
    """Search a Monday.com board for items matching a search term."""
    # Monday.com doesn't support GraphQL variables inside query_params,
    # so we safely embed the search term directly in the query string.
    safe_term = search_term.replace('\\', '\\\\').replace('"', '\\"')
    query = f"""
    query ($boardId: [ID!]!) {{
        boards(ids: $boardId) {{
            items_page(limit: 10, query_params: {{rules: [{{column_id: "name", compare_value: ["{safe_term}"], operator: contains_text}}]}}) {{
                items {{
                    id
                    name
                    column_values {{
                        id
                        text
                        value
                    }}
                }}
            }}
        }}
    }}
    """
    result = monday_query(query, {"boardId": [str(board_id)]})
    items = result.get("data", {}).get("boards", [{}])[0].get("items_page", {}).get("items", [])
    return items
 
 
def search_accounts(search_term):
    """Search the F&E Accounts board for a distributor."""
    items = search_board(ACCOUNTS_BOARD_ID, search_term)
    if items:
        return {"id": items[0]["id"], "name": items[0]["name"]}
    return None
 
 
def create_watchlist_item(name, column_values):
    """Create a new item on the F & E Watchlist board."""
    query = """
    mutation ($boardId: ID!, $name: String!, $columnValues: JSON!) {
        create_item(board_id: $boardId, item_name: $name, column_values: $columnValues) {
            id
            name
        }
    }
    """
    result = monday_query(query, {
        "boardId": str(WATCHLIST_BOARD_ID),
        "name": name,
        "columnValues": json.dumps(column_values),
    })
    return result["data"]["create_item"]
 
 
def create_update(item_id, body):
    """Post an update (comment) on a Monday.com item."""
    query = """
    mutation ($itemId: ID!, $body: String!) {
        create_update(item_id: $itemId, body: $body) {
            id
        }
    }
    """
    return monday_query(query, {"itemId": str(item_id), "body": body})
 
 
def create_subitem(parent_item_id, name):
    """Create a subitem under a parent item and assign to Jordan Soles."""
    query = """
    mutation ($parentId: ID!, $name: String!, $columnValues: JSON!) {
        create_subitem(parent_item_id: $parentId, item_name: $name, column_values: $columnValues) {
            id
            name
        }
    }
    """
    column_values = {
        "person": {"personsAndTeams": [{"id": JORDAN_SOLES_USER_ID, "kind": "person"}]}
    }
    result = monday_query(query, {
        "parentId": str(parent_item_id),
        "name": name,
        "columnValues": json.dumps(column_values),
    })
    return result["data"]["create_subitem"]
 
 
# ── Article & Claude helpers ────────────────────────────────────────────────
 
def fetch_article(url):
    """Fetch article content from a URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.text
 
 
def extract_project_from_article(article_html, url):
    """Use Claude to extract project info from a news article."""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Extract project information from this entertainment news article. Return a JSON object with these fields:
 
- title: The film or TV show title
- description: A one-paragraph logline/synopsis
- summary: A 2-4 sentence summary of the article's key points
- director: Director name(s) if mentioned
- writer: Writer name(s) if mentioned
- cast: Key cast members if mentioned
- studio: Studio or distributor name
- production_status: One of: Pre-Production, In Production, Filming, Post-Production, Released, In Development, Announced, Script, On Hold, Completed, Rumored
- genre: Genre(s) comma-separated
- type: Either "VFX Film" or "VFX Episodic"
- source_name: The publication name (e.g., "Deadline", "Variety", "THR")
 
If a field isn't mentioned in the article, use null.
 
Article URL: {url}
 
Article HTML:
{article_html[:15000]}
 
Return ONLY valid JSON, no other text."""
        }]
    )
    text = response.content[0].text.strip()
    # Try to extract JSON from the response
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        return json.loads(json_match.group())
    return json.loads(text)
 
 
def map_production_status(status):
    """Map a production status string to the Monday.com label."""
    if not status:
        return "Development Unknown"
    return PRODUCTION_STATUS_MAP.get(status.lower(), "Development Unknown")
 
 
# ── Routes ──────────────────────────────────────────────────────────────────
 
@app.route("/")
def index():
    return render_template("index.html")
 
 
@app.route("/api/process", methods=["POST"])
def process_url():
    """Main endpoint: process a URL and create/update Monday.com opportunity."""
    data = request.json
    url = data.get("url", "").strip()
    imdb_data = data.get("imdb_data")  # Optional: from bookmarklet
 
    if not url and not imdb_data:
        return jsonify({"error": "Please provide a URL"}), 400
 
    steps = []
    is_imdb_pro = url and "pro.imdb.com" in url
 
    try:
        # ── Step 1: Extract project info ────────────────────────────────
        if imdb_data:
            # Data came from the bookmarklet
            project = imdb_data
            is_imdb_pro = True
            steps.append({"step": "Extract", "status": "done", "detail": f"Received IMDb Pro data for: {project.get('title', 'Unknown')}"})
        elif is_imdb_pro:
            # IMDb Pro URL without bookmarklet data - we can't scrape it server-side
            return jsonify({
                "error": "IMDb Pro requires the bookmarklet to extract data. Please use the bookmarklet while on the IMDb Pro page, or paste a news article URL instead."
            }), 400
        else:
            # News article
            steps.append({"step": "Fetch", "status": "working", "detail": f"Reading article from {url}"})
            article_html = fetch_article(url)
            steps[-1]["status"] = "done"
 
            steps.append({"step": "Extract", "status": "working", "detail": "Analyzing article with AI..."})
            project = extract_project_from_article(article_html, url)
            steps[-1]["status"] = "done"
            steps[-1]["detail"] = f"Identified project: {project.get('title', 'Unknown')}"
 
        title = project.get("title")
        if not title:
            return jsonify({"error": "Could not identify a project title from the content"}), 400
 
        # ── Step 2: Search Monday.com ───────────────────────────────────
        steps.append({"step": "Search", "status": "working", "detail": f"Searching Monday.com for \"{title}\"..."})
 
        existing_item = None
        existing_board = None
 
        # Search Watchlist
        watchlist_results = search_board(WATCHLIST_BOARD_ID, title)
        if watchlist_results:
            existing_item = watchlist_results[0]
            existing_board = "F & E Watchlist"
 
        # Search Deal Tracker
        if not existing_item:
            tracker_results = search_board(DEAL_TRACKER_BOARD_ID, title)
            if tracker_results:
                existing_item = tracker_results[0]
                existing_board = "F & E Deal Tracker"
 
        if existing_item:
            steps[-1]["status"] = "done"
            steps[-1]["detail"] = f"Found existing opportunity on {existing_board}: \"{existing_item['name']}\""
        else:
            steps[-1]["status"] = "done"
            steps[-1]["detail"] = "No existing opportunity found"
 
        # ── Step 3: Create or use existing ──────────────────────────────
        item_id = None
        item_name = None
        created_new = False
 
        if existing_item:
            item_id = existing_item["id"]
            item_name = existing_item["name"]
        else:
            steps.append({"step": "Create", "status": "working", "detail": "Creating new opportunity on F & E Watchlist..."})
 
            column_values = {
                WATCHLIST_COLUMNS["description"]: project.get("description", "") or "",
                WATCHLIST_COLUMNS["stage"]: {"label": "Watchlist"},
                WATCHLIST_COLUMNS["production_status"]: {"label": map_production_status(project.get("production_status"))},
                WATCHLIST_COLUMNS["type"]: project.get("type", "") or "",
                WATCHLIST_COLUMNS["genre"]: project.get("genre", "") or "",
            }
 
            # Add IMDb Pro URL if available
            imdb_url = project.get("imdb_pro_url") or (url if is_imdb_pro else "")
            if imdb_url:
                column_values[WATCHLIST_COLUMNS["imdb_pro"]] = imdb_url
 
            # Search for the account/distributor
            studio = project.get("studio") or project.get("distributor")
            account = None
            if studio:
                account = search_accounts(studio)
                if account:
                    column_values[WATCHLIST_COLUMNS["accounts"]] = {"item_ids": [int(account["id"])]}
 
            new_item = create_watchlist_item(title, column_values)
            item_id = new_item["id"]
            item_name = new_item["name"]
            created_new = True
 
            steps[-1]["status"] = "done"
            steps[-1]["detail"] = f"Created: \"{item_name}\" (linked to {account['name'] if account else 'no account'})"
 
        # ── Step 4: Post Item Update (news article only) ────────────────
        if not is_imdb_pro:
            steps.append({"step": "Update", "status": "working", "detail": "Posting article summary..."})
 
            summary = project.get("summary", "No summary available.")
            source_name = project.get("source_name", "News Source")
            from datetime import date
            today = date.today().strftime("%B %d, %Y")
 
            update_body = (
                f"<h3>📰 News Update — {source_name} ({today})</h3>"
                f"<p>{summary}</p>"
                f"<p><b>Source:</b> <a href=\"{url}\">{url}</a></p>"
            )
            create_update(item_id, update_body)
 
            steps[-1]["status"] = "done"
            steps[-1]["detail"] = f"Posted article summary from {source_name}"
 
        # ── Step 5: Determine account name for subitem ──────────────────
        account_name = "studio"
        if not is_imdb_pro and project.get("studio"):
            account = search_accounts(project["studio"])
            if account:
                account_name = account["name"]
        elif is_imdb_pro and project.get("distributor"):
            account = search_accounts(project["distributor"])
            if account:
                account_name = account["name"]
 
        # If we created the item and found an account earlier, use that
        if created_new and studio:
            found = search_accounts(studio)
            if found:
                account_name = found["name"]
 
        # ── Step 6: Create subitem ──────────────────────────────────────
        steps.append({"step": "Subitem", "status": "working", "detail": "Creating follow-up subitem..."})
 
        subitem_name = f"Please look into {item_name} and email appropriate {account_name}"
        create_subitem(item_id, subitem_name)
 
        steps[-1]["status"] = "done"
        steps[-1]["detail"] = f"Created: \"{subitem_name}\" (assigned to Jordan Soles)"
 
        # ── Done ────────────────────────────────────────────────────────
        return jsonify({
            "success": True,
            "title": item_name,
            "created_new": created_new,
            "existing_board": existing_board if not created_new else None,
            "monday_url": f"https://rodeofx-league.monday.com/boards/{WATCHLIST_BOARD_ID}/pulses/{item_id}",
            "steps": steps,
        })
 
    except Exception as e:
        steps.append({"step": "Error", "status": "error", "detail": str(e)})
        return jsonify({"error": str(e), "steps": steps}), 500
 
 
@app.route("/api/imdb-receive", methods=["POST"])
def receive_imdb_data():
    """Endpoint for the bookmarklet to send IMDb Pro data."""
    data = request.json
    # Store temporarily or process directly
    return jsonify({"success": True, "data": data})
 
 
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")
