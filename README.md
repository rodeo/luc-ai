# LUC AI — Rodeo FX

Live at: **https://lucai.ai**

LUC AI is a web tool for the Film & Episodic team to quickly log opportunities from news articles (Deadline, Variety, THR) or IMDb Pro into Monday.com.

## What it does

1. **Paste a news article URL** → The app reads the article, uses AI to extract the project details, searches Monday.com to check if the opportunity already exists, creates or updates it, posts an article summary as an Item Update, and creates a follow-up subitem assigned to Jordan Soles.

2. **Use the IMDb Pro bookmarklet** → While browsing IMDb Pro, click the bookmarklet to scrape project data and send it to the app. It creates/updates the opportunity and adds a follow-up subitem (no Item Update for IMDb Pro links).

## Deploy to Render (free tier)

### Step 1: Push code to GitHub

Create a new GitHub repo (e.g., `luc-ai`) and push this folder to it:

```bash
cd news-to-monday-webapp
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/luc-ai.git
git push -u origin main
```

### Step 2: Create a Render account

Go to [render.com](https://render.com) and sign up (free). Connect your GitHub account.

### Step 3: Create a new Web Service

1. Click **New** → **Web Service**
2. Connect your `luc-ai` repo
3. Configure:
   - **Name:** `luc-ai`
   - **Region:** Oregon (or closest to your team)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn --bind 0.0.0.0:$PORT --workers 2 app:app`
   - **Instance Type:** Free
4. Add environment variables (under **Environment**):
   - `MONDAY_API_TOKEN` = your Monday.com API token
   - `ANTHROPIC_API_KEY` = your Anthropic API key
5. Click **Create Web Service**

Render will build and deploy. You'll get a URL like `luc-ai.onrender.com`.

### Step 4: Connect your domain (lucai.ai)

**In Render:**
1. Go to your web service → **Settings** → **Custom Domains**
2. Click **Add Custom Domain**
3. Enter `lucai.ai` (or `app.lucai.ai` if you want a subdomain)
4. Render will show you DNS records to configure

**In Squarespace DNS settings:**

For the root domain (`lucai.ai`):
- Add an **A record** pointing to Render's IP address (Render will provide this)
- Add a **CNAME record** for `www` pointing to `luc-ai.onrender.com`

For a subdomain like `app.lucai.ai`:
- Add a **CNAME record**: Host = `app`, Value = `luc-ai.onrender.com`

To find DNS settings in Squarespace:
1. Go to [account.squarespace.com](https://account.squarespace.com)
2. Click on your domain (`lucai.ai`)
3. Go to **DNS** → **DNS Settings**
4. Click **Add Record** and enter the records above

SSL is automatic — Render provisions a free certificate once DNS propagates (usually 10-30 minutes).

### Step 5: Get your API keys

**Monday.com API Token:**
1. Log into Monday.com
2. Click your profile picture (bottom-left) → **Developers**
3. Go to **My Access Tokens**
4. Copy your personal API token
5. Make sure your account has access to the FILM & EPISODIC workspace

**Anthropic API Key:**
1. Go to [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)
2. Create a new key
3. Note: Claude API usage is pay-per-use (each article analysis costs ~$0.01-0.02)

## Running locally (for development)

```bash
cp .env.example .env
# Edit .env with your API keys
pip install -r requirements.txt
python app.py
```

The app will be available at http://localhost:5000

## Using the IMDb Pro bookmarklet

1. Open the app at https://lucai.ai
2. Scroll down to the "IMDb Pro Bookmarklet" section
3. Drag the "Send to LUC AI" button to your bookmarks bar
4. When you're on an IMDb Pro project page, click the bookmarklet
5. It will scrape the page and send the data to the app automatically

**Note:** The bookmarklet works on desktop browsers. On mobile, just paste news article URLs directly — the article flow works fully on phones.

## Monday.com boards

| Board | ID |
|-------|----|
| F & E Watchlist | 8888736546 |
| F & E Deal Tracker | 8888736517 |
| F & E Accounts | 8888736490 |

## Tech stack

- **Backend:** Python / Flask
- **AI:** Claude (Anthropic API) for article analysis
- **CRM:** Monday.com GraphQL API
- **Frontend:** Vanilla HTML/CSS/JS (no build step)
- **Hosting:** Render (free tier)
- **Domain:** lucai.ai (Squarespace)
