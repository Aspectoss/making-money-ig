# One-Time Setup

The site runs itself after this. No daily tasks from you.

## Already automated

- [x] 4 free money tools (calculators + invoice generator)
- [x] 5 SEO guides for search traffic
- [x] Weekly blog refresh (GitHub Action, Mondays)
- [x] Auto-deploy on every push (GitHub Pages)
- [x] Agent rules so Cursor maintains it

**Site:** https://aspectoss.github.io/making-money-ig/

## You do this once (5 minutes)

### Step 1: Amazon Associates (or skip for now)

1. Go to https://affiliate-program.amazon.com and sign up (free)
2. Get your associate tag (looks like `yourname-20`)

### Step 2: Paste into secrets

```powershell
cd "c:\Users\kyled\OneDrive\Documents\making money ig"
Copy-Item secrets.example.json secrets.json -ErrorAction SilentlyContinue
```

Edit `secrets.json`:
- `amazon_associate_tag`: your tag
- Replace affiliate URLs when you get approved for programs (FreshBooks, YNAB, etc.)

Then:
```powershell
python scripts/build-config.py
git add site/js/config.js
git commit -m "Add affiliate config"
git push
```

### Step 3: Nothing else

The site earns when people find your tools on Google and click affiliate links. The agent adds more SEO content every week automatically.

## Optional upgrades (tell the agent)

- Add Google AdSense after traffic grows
- Add Stripe payment link for premium invoice templates
- Add more calculator tools for more search keywords
