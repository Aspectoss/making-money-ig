# Money Machine Agent Playbook

You are operating the **Money Minute** Instagram income system. Your job is to keep the money pipeline running with minimal user input.

## Project goal

Build audience on Instagram (faceless money-tips reels), monetize via link-in-bio (affiliates + email list + digital products).

## What runs automatically (do not redo unless broken)

- **GitHub Action `weekly-content.yml`**: Every Sunday, generates a new `content/week-*` folder and commits it.
- **GitHub Action `deploy-pages.yml`**: On every push to `main`, deploys `site/` to GitHub Pages.
- **`scripts/daily.ps1`**: Shows today's post from the latest content week.

## Your default workflow when the user opens this project

1. Run `powershell -File scripts/daily.ps1` and report today's reel (hook, caption path, post time).
2. Check `secrets.json` exists. If affiliate links are still placeholders, remind user to fill them once, then run `scripts/sync-site.ps1`.
3. If no content for today, run `python generate.py`.
4. If user asks you to "make money" or "keep going", prioritize:
   - Getting today's reel posted (give them copy-paste caption + on-screen text)
   - Updating affiliate links when user provides them
   - Building Gumroad product copy if they want to sell templates
   - Local business outreach scripts ($150/reel side hustle)

## What you must NOT do

- Do not automate Instagram login, posting, or DMs (ToS violation, account ban risk).
- Do not commit `secrets.json` (contains affiliate URLs).
- Do not promise guaranteed income.

## File map

| Path | Purpose |
|------|---------|
| `generate.py` | Creates 7 days of reel content |
| `content/week-*/day-*/` | Script, caption, on-screen text per post |
| `site/` | Link-in-bio page (auto-deployed) |
| `secrets.json` | Affiliate + Formspree config (local only) |
| `config.json` | IG bio, hashtags, content settings |

## Monetization ladder

1. Post daily reels (user films in CapCut, 15 min/day)
2. Bio links to GitHub Pages site (`site/index.html`)
3. Free guide at `site/guide.html` builds trust
4. Affiliate links in `secrets.json` earn per signup
5. Sell $9 Gumroad template when audience grows

## When user says "set it up" or "make money for me"

Execute in order:
1. `python generate.py` if no recent content week
2. `powershell -File scripts/sync-site.ps1`
3. `powershell -File scripts/daily.ps1`
4. Tell user exactly one action: post today's reel OR paste affiliate link they need to sign up for

## GitHub Pages URL

After first deploy: `https://aspectoss.github.io/making-money-ig/`

Put this in Instagram bio once account is created.
