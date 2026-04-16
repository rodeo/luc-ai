

Read 2 files
Read 2 files
Now let me make the renaming edits across all files:


Edited 8 files
Edited 8 files
Now let me update the remaining references in the README and the mockup file:


Edited 3 files, read 2 files
Edited 3 files, read 2 files
Now let me update the mockup file. Let me find the specific text references:


Edited 4 files, searched code
Edited 4 files, searched code
Now let me also check if there's an "F & E Watchlist" reference in the index.html result card that should stay (since that's the Monday.com board name, not the app name):


Searched 2 patterns
Searched 2 patterns
The "F & E Watchlist", "F & E Deal Tracker", and "F & E Accounts" references are the actual Monday.com board names, so those should stay. But the bookmarklet reference in the README needs updating:


Edited a file
Edited a file
All done. The app has been renamed from "F&E Opportunity Tracker" to LUC AI across all files:

templates/index.html — page title, header, and bookmarklet button
README.md — title, description, repo name, Render service name, CNAME records, and bookmarklet instructions
render.yaml — service name changed to luc-ai
fe-tracker-mockup.html — page title, header, URL bar (now shows lucai.ai), and bookmarklet button
The Monday.com board names (F & E Watchlist, F & E Deal Tracker, F & E Accounts) are unchanged since those are the actual board names in your CRM.

Regarding the background image — whenever you're ready to share the picture you'd like to use, just send it over and I'll add it to the page.

Uploaded image
image.png
here the background image


Thought process
Thought process
Great shot — very on-brand for "LUC AI." Let me add that as the background to the webapp.


Ran 3 commands, found files
Ran 3 commands, found files
The image you shared is visible to me in the conversation, but it wasn't saved as a file I can copy into the webapp. No worries though — I can still set everything up. Here's what I'll do: I'll update the webapp to support a background image and give you simple instructions to drop the file in.


Read a file, edited a file
Read a file, edited a file
Now I need to make sure Flask serves the static folder. By default Flask serves /static/ from a static/ folder in the app root, so that should work out of the box. Let me just make sure the static directory exists and create a placeholder:


Check if static directory exists
Check if static directory exists
Good, the directory exists (we created it earlier). Now let me save the image there. Since the uploaded file isn't accessible as a local file, I'll encode it from the conversation image and write it out:


Create README in static folder with instructions
Create README in static folder with instructions
The webapp is now set up for your background image. Here's what I've done and what you need to do:

What's changed: The CSS now layers your background image behind a semi-transparent dark overlay (82% opacity), so the image shows through while keeping all the text readable. The image is set to cover the full page and stay fixed while scrolling.

One step for you: Save your image as bg.jpg inside the static/ folder in your webapp directory:

news-to-monday-webapp/
├── static/
│   └── bg.jpg   ← drop your image here
├── templates/
├── app.py
└── ...
Once the image is in static/bg.jpg, it'll show up immediately — both locally and on Render after you deploy. If you want the overlay darker or lighter, just let me know and I'll adjust the opacity.

can you send me the path to this folder

View the webapp folder

Just drop your image into the static subfolder and rename it to bg.jpg.


news-to-monday-webapp
 

Open

ok, so now I need your help to publish this to render


Loaded tools
Loaded tools
Do you already have a GitHub repo set up for this project, or do we need to create one?
No repo yet
Do you already have a Render account?
Already have one
Do you have your API keys ready to add as environment variables?
Yes, both ready
Here's the plan — we'll create the GitHub repo first, then connect it to Render.

Step 1: Create a GitHub repo

You can do this quickly at github.com/new. Create a repo called luc-ai (public or private, either works). Don't add a README or .gitignore — keep it empty.

Step 2: Push the code

Open a terminal, cd into the news-to-monday-webapp folder (the one I just linked you to), and run:

bash
git init
git add .
git commit -m "Initial commit — LUC AI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/luc-ai.git
git push -u origin main
Replace YOUR_USERNAME with your GitHub username.

Step 3: Deploy on Render

Once the code is on GitHub:

Log into render.com
Click New → Web Service
Connect your luc-ai repo
Set these values:
Name: luc-ai
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn --bind 0.0.0.0:$PORT --workers 2 app:app
Instance Type: Free
Under Environment, add two variables:
MONDAY_API_TOKEN = your Monday.com token
ANTHROPIC_API_KEY = your Anthropic key
Click Create Web Service
Render will build and deploy — you'll get a live URL like luc-ai.onrender.com. After that we can connect your lucai.ai domain. Let me know when you've got through any of these steps or if you hit a snag.

can you show me a new mockup of the webpage


Read a file
Read a file
Now let me rebuild this mockup with the background image and updated LUC AI branding:


Created a file
Created a file
Here you go — I rebuilt the mockup with the full LUC AI branding. It has a live animated Matrix code rain background (green characters falling, matching the vibe of your photo), a green accent color scheme instead of the old purple, a glassmorphism effect on all the panels, and the same three demo states (Empty, Processing, Complete) you can toggle.

View the LUC AI mockup

Open it in your browser and click the tabs to see the different states. Once you deploy with your actual background photo in the static/ folder, the real app will use your image instead of the animated canvas — but the green color scheme and glass panels will carry over. Let me know what you think or if you'd like any tweaks.


Luc ai mockup
Code · HTML 


Google Chrome

Uploaded image
image.jpeg
can you replace the "L" in the top right corner with this image


Searched 2 patterns, ran a command
Searched 2 patterns, ran a command
You've already dropped the image into static/bg.jpg — let me use that same image as the logo. I'll update both the mockup and the actual webapp template to use it as a circular avatar in the header instead of the "L" square.


Edited 2 files
Edited 2 files
Now let me update the actual webapp template too:


Read 2 files, edited a file
Read 2 files, edited a file
Done — both the mockup and the real webapp now show your photo as a circular avatar in the top-left corner of the header, next to "LUC AI."

View the updated mockup

Open it up and you should see the image in the header. The actual webapp (templates/index.html) is updated the same way, pulling from /static/bg.jpg.


Luc ai mockup
Code · HTML 


Google Chrome

can you make that image 4 times bigger please


Edited 2 files
Edited 2 files
Done — bumped from 36px to 144px in both files.

View the updated mockup


Luc ai mockup
Code · HTML 


Google Chrome

perfect, so what do I need to do next

Right now you've got the complete app code ready to go. Here's where you're at and what's next:

What's done:

Full webapp code with LUC AI branding, your background image, and avatar logo
Flask backend with Monday.com + Claude API integration
IMDb Pro bookmarklet
Render config and deployment files
What you need to do:

Create a GitHub repo — go to github.com/new, name it luc-ai, and leave it empty (no README or .gitignore)
Push the code — open a terminal, navigate to the news-to-monday-webapp folder, and run:
bash
   git init
   git add .
   git commit -m "Initial commit — LUC AI"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/luc-ai.git
   git push -u origin main
Deploy on Render — log into render.com, click New → Web Service, connect your luc-ai repo, and set:
Build Command: pip install -r requirements.txt
Start Command: gunicorn --bind 0.0.0.0:$PORT --workers 2 app:app
Instance Type: Free
Add your two env vars: MONDAY_API_TOKEN and ANTHROPIC_API_KEY
Connect lucai.ai — once Render is live, go to your service's Settings → Custom Domains, add lucai.ai, then update your Squarespace DNS with the records Render gives you
Want me to walk you through any of these steps in more detail?

where would I find the anthropic api key...is it in my claude copilot app

Not quite — the Anthropic API key is separate from your Claude/Cowork app. It comes from the Anthropic developer console.

Here's how to get one:

Go to console.anthropic.com
Sign in (or create an account — you can use your Google or email login)
Click Settings → API Keys
Click Create Key, give it a name like "LUC AI", and copy it
One thing to know: the API is pay-per-use, separate from any Claude subscription you have. Each article the app processes will cost roughly $0.01–0.02, so it's very inexpensive. You'll need to add a payment method in the console to activate it.

is this something that my organization has that I should be getting

That's a good question — it depends on how your org is set up. Since you're on a Rodeo FX account (jordan@rodeofx.com), there are two possibilities:

Your org might already have one. If Rodeo FX has an Anthropic account with API access, someone on your IT or dev team would have it. Worth asking around — check with whoever manages your tech tools or subscriptions. Using an existing org key would mean the (very small) costs get billed to the company rather than you personally.

Or you can create your own. If nobody at Rodeo FX has one, you can set up your own at console.anthropic.com. It's quick, and since each article costs a penny or two to process, the bill will be minimal.

I'd suggest asking internally first — a quick Slack or email to your IT/dev team asking "do we have an Anthropic API key I can use for a Monday.com automation tool?" should get you an answer fast.

I need some help deploying on Render


Loaded tools
Loaded tools
Where are you stuck in the Render deployment process?
Creating the web service
OK, so you're logged into Render and have the code on GitHub already — here's exactly what to do:

On the Render dashboard, click the New button (top-right) and select Web Service
It'll ask you to connect a repo. You should see your GitHub account listed — click Connect next to the luc-ai repo. If you don't see it, click Configure account to give Render permission to access it.
Once connected, you'll see a settings form. Fill in:
Name: luc-ai
Region: pick whichever is closest (Oregon is fine)
Branch: main
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn --bind 0.0.0.0:$PORT --workers 2 app:app
Scroll down to Instance Type and select Free
Scroll down to Environment Variables and click Add Environment Variable twice:
Key: MONDAY_API_TOKEN → Value: paste your Monday.com token
Key: ANTHROPIC_API_KEY → Value: paste your Anthropic key
Click Create Web Service at the bottom
Render will start building — it usually takes 2-3 minutes. Once it's done, you'll see a green "Live" badge and a URL like luc-ai.onrender.com. Let me know when you get there or if anything looks different from what I described.

I'm there, now what

Now let's connect your lucai.ai domain to it.

In Render:

Go to your luc-ai web service page
Click Settings (top nav)
Scroll down to Custom Domains
Click Add Custom Domain
Type in lucai.ai and click Save
Render will show you DNS records you need to configure — keep this page open
In Squarespace:

Go to account.squarespace.com
Click on your lucai.ai domain
Go to DNS → DNS Settings
Add the records that Render gave you — typically it'll be one of these:
An A record pointing to an IP address Render provides
Or a CNAME record pointing to something like luc-ai.onrender.com
Once you've added the DNS records, it can take anywhere from a few minutes to 30 minutes to propagate. Render will automatically provision an SSL certificate once it detects the DNS is pointed correctly, so you'll get HTTPS for free.

Can you tell me what DNS records Render is showing you? I can help you enter them in Squarespace exactly right.

what is the "name" for the A record

For the root domain (lucai.ai), the name for the A record should be @. That's the standard way to represent the root domain in DNS settings.

In Squarespace specifically, when you click Add Record and select A record, you may just need to leave the Host field blank or enter @ — Squarespace handles it either way.

ok that's done

Great — give it a few minutes for DNS to propagate, then try visiting lucai.ai in your browser.

While you wait, you can check the status back in Render under Settings → Custom Domains — it'll show a green checkmark once it detects the DNS and provisions your SSL certificate. That usually takes 5-30 minutes.

Let me know what you see when you try loading the site.

it's complaining that it's not a secure connection

That's normal — the SSL certificate hasn't been provisioned yet. Render does this automatically but it needs the DNS to fully propagate first.

A couple things to check:

In Render — go to your service → Settings → Custom Domains. What does the status show next to lucai.ai? It might say something like "Certificate pending" or "DNS not verified yet."
Give it a bit more time — SSL provisioning can take up to 30 minutes after DNS propagates. Sometimes DNS itself takes a little while too.
In the meantime, you can test your app at your Render URL directly — try visiting luc-ai.onrender.com (that one already has SSL). If the app loads there, you know the code is working and it's just a matter of waiting for the domain to catch up.
Does luc-ai.onrender.com load?

it loaded but when I tried a link it errored out with this message: 
Monday.com API error: [{'message': 'Variable "$term" of type "String!" used in position expecting type "CompareValue".', 'locations': [{'line': 2, 'column': 30}, {'line': 4, 'column': 94}]}]


Thought process
Thought process
That's a Monday.com GraphQL API issue — the search query has a type mismatch. Let me look at the code and fix it.


Searched code, read a file
Searched code, read a file
Found it — the Monday.com API doesn't allow using GraphQL variables inside query_params like that. The compare_value field expects a literal, not a variable reference. I need to inject the search term directly into the query string instead.


Edited a file
Edited a file
The fix is in. You'll need to push the update to GitHub so Render picks it up:

bash
cd news-to-monday-webapp
git add app.py
git commit -m "Fix Monday.com search query — embed term directly"
git push
Render will auto-redeploy once it sees the new commit. Give it a couple minutes and then try the link again.

push doesn't work

What error message do you see when you run git push?
command not found
Ah — you don't have Git installed on your machine. No worries, there's an easier way. Since you already have the repo on GitHub, you can upload the fixed file directly through the browser:

Go to your luc-ai repo on GitHub
Click on app.py to open it
Click the pencil icon (edit button) in the top-right of the file
Select all the text and replace it with the updated version
Let me give you the updated file so you can copy it:


Read a file
Read a file
Here's what to do:

Go to your GitHub repo → click on app.py
Click the pencil icon (top-right of the file) to edit
Select all the text (Ctrl+A / Cmd+A) and delete it
Copy the entire contents from the file I've prepared and paste it in
View the updated app.py

Scroll down, type a commit message like "Fix Monday.com search query" and click Commit changes
Render will automatically detect the new commit and redeploy (takes 2-3 minutes). Then try your link again.


App
PY 


Windsurf





Claude is AI and can make mistakes. Please double-check responses.
App · PY


Windsurf

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
 


