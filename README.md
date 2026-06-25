# Making Money on Instagram (Starter System)

This folder is a working starter kit, not a promise of income. Money comes from **posting content**, **driving link-in-bio clicks**, and **selling or recommending something useful**. This system automates the hard part: what to post and how to monetize it.

## What is already built

1. **`generate.py`** - Creates 7 days of faceless reel scripts, captions, on-screen text, and a posting checklist.
2. **`bio-page/index.html`** - Link-in-bio page for affiliate links and email capture.
3. **`config.json`** - Account bio, hashtags, and affiliate URL placeholders.

## Your 60-minute launch plan

### Step 1: Generate this week's content (2 min)

```powershell
cd "c:\Users\kyled\OneDrive\Documents\making money ig"
python generate.py
```

Open the new folder under `content/week-YYYY-MM-DD/CHECKLIST.md`.

### Step 2: Create the Instagram account (10 min)

- Pick a username from `config.json` or similar.
- Switch to **Business** or **Creator** account.
- Bio: copy from `config.json`.
- Profile photo: make a simple logo in [Canva](https://www.canva.com) (free).

### Step 3: Deploy link-in-bio (10 min)

1. Go to [Netlify Drop](https://app.netlify.com/drop).
2. Drag the `bio-page` folder onto the page.
3. You get a free URL like `random-name.netlify.app`.
4. Put that URL in your Instagram bio.

Edit `bio-page/index.html` first and replace the `LINKS` object with real URLs.

### Step 4: Make and post your first reel (30 min)

For `content/week-.../day-01/`:

1. Open CapCut (free) or Instagram Reels editor.
2. Add stock clips (your screen, wallet, laptop, etc.).
3. Add text from `on-screen-text.txt` every few seconds.
4. Use a trending audio from the Reels tab.
5. Post with text from `caption.txt`.

Repeat daily using the checklist.

## How this actually makes money

| Stage | What you do | Realistic income |
|-------|-------------|------------------|
| Week 1-2 | Post daily, reply to comments | $0 (building audience) |
| Week 3+ | Free PDF guide in bio (Gumroad $0+ or Google Drive) | Email list + trust |
| Week 4+ | Affiliate links in bio (banks, apps, Amazon) | $20-200/mo early |
| Month 2+ | Sell $9-29 digital template/guide | $100-500/mo if consistent |
| 5k+ followers | Brand DM deals, shoutouts | Varies |

Affiliate programs to sign up for (free):

- Amazon Associates
- Impact / CJ (finance apps, software)
- Gumroad (sell your own PDF/template, 10% fee)

## Regenerate content anytime

```powershell
python generate.py
```

Each run creates a new `content/week-...` folder with fresh scripts.

## What I cannot do for you

- Post to Instagram automatically (against ToS, risks ban)
- Guarantee earnings
- Sign up for affiliate accounts on your behalf

You post. The system gives you the content and monetization structure.

## Next upgrades (ask and I can build)

- Lead magnet PDF generator
- Outreach scripts for local video clients ($150/reel side hustle)
- Notion template to sell on Gumroad
- Batch CapCut project notes per niche
