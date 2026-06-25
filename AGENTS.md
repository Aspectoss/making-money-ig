# MoneyTools Agent Playbook

You operate an **automated affiliate tools site**. No Instagram. No manual posting. Income comes from search traffic and affiliate clicks.

## Live URL

https://aspectoss.github.io/making-money-ig/

## Default workflow

1. Run `python generate_seo.py` and `python scripts/build-config.py` if site content is stale.
2. Improve tools, add new calculators, or write more SEO articles when asked.
3. Push to `main` — GitHub Actions deploys automatically.
4. Never ask the user to post on social media.

## Monetization

- Affiliate links in `secrets.json` → `site/js/config.js`
- User only needs to paste affiliate tag once (Amazon Associates, etc.)
- Tools: freelance rate, invoice generator, compound interest, subscription audit

## Adding a new tool

1. Create `site/tools/your-tool.html` using existing tools as template.
2. Add card to `site/index.html`.
3. Add SEO article to `ARTICLES` in `generate_seo.py`.
4. Run generators, commit, push.

## What you must NOT do

- Revert to Instagram content strategy unless user asks.
- Commit `secrets.json`.
- Promise specific income amounts.

## Maintenance tasks (do proactively)

- Add more long-tail SEO articles to `generate_seo.py`
- Improve tool UX and meta descriptions for SEO
- Submit sitemap ideas (could add sitemap.xml later)
- Monitor GitHub Actions for failed deploys
