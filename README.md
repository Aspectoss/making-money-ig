# MoneyTools — Automated Income Site

Fully automated web tools that earn via affiliate commissions. No posting, no daily manual work.

**Live site:** https://aspectoss.github.io/making-money-ig/

## What runs without you

| Automation | Schedule |
|------------|----------|
| SEO blog refresh | Every Monday (GitHub Action) |
| Site deploy | Every push to `main` |
| Cursor agent | Maintains tools when you ask |

## Your one-time setup (5 min)

1. Sign up for [Amazon Associates](https://affiliate-program.amazon.com) (or any affiliate program)
2. Copy `secrets.example.json` to `secrets.json`
3. Paste your affiliate tag / links
4. Run `python scripts/build-config.py` and push (or tell the agent to do it)

That is it. Traffic and commissions grow over time from search.

## Local commands

```powershell
python generate_seo.py          # regenerate blog articles
python scripts/build-config.py  # sync affiliate links to site
```

## How money is made

- **Affiliate clicks** on invoicing, budgeting, and savings tools (high-intent users)
- **Search traffic** from auto-generated SEO guides
- Optional: add `premium_stripe_url` in secrets for paid invoice templates later

## Agent instructions

See `AGENTS.md` for the full autopilot playbook.
