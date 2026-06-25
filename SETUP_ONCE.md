# One-Time Setup (10 minutes)

Do these once. After that, the agent and GitHub Actions handle content and site deploy.

## Already done by the agent

- [x] Content generator (`generate.py`)
- [x] This week's reels in `content/week-*`
- [x] Link-in-bio site in `site/`
- [x] Weekly auto-content (GitHub Action)
- [x] Auto-deploy site on push (GitHub Pages)
- [x] Cursor agent rules + session hook

## You do these 4 things once

### 1. Create Instagram account (5 min)

- Username: pick from `config.json` suggestions
- Bio: copy from `config.json`
- Switch to Business/Creator account
- Bio link: `https://aspectoss.github.io/making-money-ig/` (after GitHub push)

### 2. Copy secrets file (1 min)

```powershell
cd "c:\Users\kyled\OneDrive\Documents\making money ig"
Copy-Item secrets.example.json secrets.json
powershell -File scripts\sync-site.ps1
```

Edit `secrets.json` when you have real affiliate links.

### 3. Sign up for affiliates (optional, do when ready)

| Program | Sign up | What to paste in secrets.json |
|---------|---------|--------------------------------|
| Amazon Associates | affiliate-program.amazon.com | product links later |
| Formspree (email) | formspree.io (free) | `email_capture.formspree_endpoint` |
| Gumroad (sell PDF) | gumroad.com | `gumroad.template_product_url` |

### 4. Post your first reel (15 min)

```powershell
powershell -File scripts\daily.ps1
```

Open the folder it prints. CapCut + stock clips + on-screen text. Paste caption. Post.

## What happens automatically after GitHub push

| When | What |
|------|------|
| Every push to `main` | Site deploys to GitHub Pages |
| Every Sunday 2pm UTC | New week of reel content generated and committed |
| Every Cursor session | Agent sees today's post task |

## Daily routine (you, 15 min/day)

1. Open this project in Cursor (or say "what's today's post")
2. Agent runs `daily.ps1` and gives you caption
3. Make reel in CapCut, post to Instagram
4. Reply to comments

That is the minimum viable money machine. Income follows consistency, not magic.
