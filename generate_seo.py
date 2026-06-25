#!/usr/bin/env python3
"""Generate SEO blog articles for MoneyTools. Runs weekly via GitHub Actions."""

import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "site" / "blog"

ARTICLES = [
    {
        "slug": "how-to-price-freelance-work",
        "title": "How to Price Freelance Work Without Undercharging",
        "description": "A simple formula to set freelance rates that cover taxes, expenses, and profit.",
        "tool_link": "../tools/freelance-rate.html",
        "sections": [
            ("Why most freelancers undercharge", [
                "They copy someone else's rate without doing the math.",
                "They forget taxes, health insurance, and unpaid admin time.",
                "They price for the project, not for the hours it actually takes.",
            ]),
            ("The rate formula that works", [
                "Start with the after-tax income you need this year.",
                "Add estimated taxes back in (usually 25-35% for US freelancers).",
                "Add annual business expenses: software, gear, insurance.",
                "Divide by real billable hours, not 40 hrs x 52 weeks.",
                "Add a 10-20% profit buffer so you can say no to bad clients.",
            ]),
            ("Use our free calculator", [
                "Plug your numbers into the Freelance Rate Calculator.",
                "Round up to the nearest $5. Confidence sells.",
                "Raise rates 10% on every new client.",
            ]),
        ],
        "affiliate_key": "invoicing",
        "affiliate_title": "Track what you earn",
        "affiliate_desc": "Once you know your rate, track invoices so you actually hit your income goal.",
        "affiliate_cta": "Compare invoicing tools",
    },
    {
        "slug": "subscription-audit-save-money",
        "title": "Subscription Audit: How to Find $200+ You Are Wasting",
        "description": "A 15-minute audit to find forgotten recurring charges draining your account.",
        "tool_link": "../tools/subscription-audit.html",
        "sections": [
            ("The zombie subscription problem", [
                "Free trials that converted. Apps you used once. Duplicate streaming services.",
                "Most people have 1-3 charges they forgot about entirely.",
            ]),
            ("15-minute audit steps", [
                "Open your bank and card statements for the last 90 days.",
                "Highlight every recurring charge. Name, cost, last time you used it.",
                "Cancel anything unused in 30 days. No exceptions.",
                "Downgrade annual plans you barely use to monthly while you decide.",
            ]),
            ("Calculate your yearly bleed", [
                "Use the Subscription Waste Calculator to total monthly spend.",
                "Multiply by 12. That number should make you angry enough to act.",
            ]),
        ],
        "affiliate_key": "budgeting",
        "affiliate_title": "Automate the audit",
        "affiliate_desc": "Budget apps surface recurring charges automatically so you do not have to dig through statements.",
        "affiliate_cta": "Try a budgeting app",
    },
    {
        "slug": "compound-interest-beginners",
        "title": "Compound Interest for Beginners: Start With $200/Month",
        "description": "Why small monthly deposits beat waiting for a big lump sum.",
        "tool_link": "../tools/compound-interest.html",
        "sections": [
            ("What compound interest actually means", [
                "You earn returns on your money, then earn returns on those returns.",
                "Time matters more than timing. Starting beats waiting for the perfect moment.",
            ]),
            ("A realistic starting plan", [
                "Build a 1-month emergency fund in savings first.",
                "Then invest a fixed amount every month, even if it is $50-200.",
                "Ignore daily market noise. Check once a year.",
            ]),
            ("Run your own numbers", [
                "Use the Compound Interest Calculator with your monthly contribution.",
                "Try 7% average return and 20 years. Adjust until the number motivates you.",
            ]),
        ],
        "affiliate_key": "savings",
        "affiliate_title": "Earn more on cash while you build",
        "affiliate_desc": "High-yield savings accounts beat traditional banks for your emergency fund.",
        "affiliate_cta": "Compare savings rates",
    },
    {
        "slug": "free-invoice-template-freelancers",
        "title": "Free Invoice Template for Freelancers (PDF in 2 Minutes)",
        "description": "Create a professional invoice in your browser without Word or Excel.",
        "tool_link": "../tools/invoice.html",
        "sections": [
            ("What every invoice needs", [
                "Your business name and contact info.",
                "Client name, invoice number, date, and due date.",
                "Line items with clear descriptions and amounts.",
                "Total due and payment instructions.",
            ]),
            ("Get paid faster", [
                "Send invoices within 24 hours of finishing work.",
                "Due date: Net 14 is standard for new clients.",
                "Follow up on day 15. Polite, direct, every time.",
            ]),
            ("Generate yours now", [
                "Use the free Invoice Generator. Fill in, preview, print or save as PDF.",
                "No signup. No watermark.",
            ]),
        ],
        "affiliate_key": "invoicing",
        "affiliate_title": "Scale beyond one-off invoices",
        "affiliate_desc": "Recurring clients deserve automated reminders and payment tracking.",
        "affiliate_cta": "Compare invoicing tools",
    },
    {
        "slug": "side-income-calculator-plan",
        "title": "Side Income Plan: How Much Extra Do You Need Per Month?",
        "description": "Work backward from a goal to a weekly side income target.",
        "tool_link": "../tools/freelance-rate.html",
        "sections": [
            ("Pick one number", [
                "Do not chase vague 'more money.' Pick a monthly target: $500, $1000, $2000.",
                "Divide by 4 for a weekly target. That is your scoreboard.",
            ]),
            ("Match effort to goal", [
                "$500/month: one small freelance gig or weekend flip.",
                "$1000/month: 2-3 clients or a $25 product sold 40 times.",
                "$2000/month: productized service with fixed scope and price.",
            ]),
            ("Price the work correctly", [
                "Use the rate calculator so side gigs do not cannibalize your main income.",
                "Say no to projects below your floor rate.",
            ]),
        ],
        "affiliate_key": "budgeting",
        "affiliate_title": "Track side income separately",
        "affiliate_desc": "See exactly how much your side hustle adds each month.",
        "affiliate_cta": "Try a budgeting app",
    },
]


def render_article(article: dict) -> str:
    date = datetime.now().strftime("%B %d, %Y")
    sections_html = ""
    for heading, bullets in article["sections"]:
        items = "".join(f"<li>{b}</li>" for b in bullets)
        sections_html += f"<h2>{heading}</h2><ul>{items}</ul>\n"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{article["title"]} — MoneyTools</title>
  <meta name="description" content="{article["description"]}" />
  <link rel="stylesheet" href="../css/main.css" />
  <script src="../js/config.js"></script>
  <script src="../js/affiliate.js"></script>
</head>
<body>
  <header>
    <div class="container">
      <a class="logo" href="../index.html">MoneyTools</a>
      <nav><a href="index.html">Guides</a></nav>
    </div>
  </header>
  <article class="container article">
    <h1>{article["title"]}</h1>
    <p class="meta">{date} &middot; 4 min read</p>
    <p>{article["description"]}</p>
    {sections_html}
    <p><a class="btn" href="{article["tool_link"]}">Use the free tool</a></p>
    <div class="affiliate-box" id="aff-box"></div>
  </article>
  <footer class="container"><p>MoneyTools — free calculators, no signup.</p></footer>
  <script>
    renderAffiliateBox("aff-box", "{article["affiliate_key"]}",
      "{article["affiliate_title"]}", "{article["affiliate_desc"]}", "{article["affiliate_cta"]}");
  </script>
</body>
</html>
"""


def render_blog_index(posts: list[dict]) -> str:
    items = "\n".join(
        f'<li><a href="{p["slug"]}.html">{p["title"]}</a><br><span style="color:var(--muted);font-size:0.85rem">{p["description"]}</span></li>'
        for p in posts
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Money Guides — MoneyTools</title>
  <meta name="description" content="Free guides on freelance pricing, subscriptions, investing, and invoicing." />
  <link rel="stylesheet" href="../css/main.css" />
</head>
<body>
  <header>
    <div class="container">
      <a class="logo" href="../index.html">MoneyTools</a>
    </div>
  </header>
  <main class="container tool-wrap">
    <h1>Money Guides</h1>
    <p class="lede">Short, practical articles. New guides added automatically every week.</p>
    <ul class="blog-list">{items}</ul>
  </main>
  <footer class="container"><p>MoneyTools</p></footer>
</body>
</html>
"""


def generate() -> Path:
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    manifest_posts = []

    for article in ARTICLES:
        path = BLOG_DIR / f"{article['slug']}.html"
        path.write_text(render_article(article), encoding="utf-8")
        manifest_posts.append(
            {
                "slug": article["slug"],
                "title": article["title"],
                "description": article["description"],
            }
        )

    (BLOG_DIR / "index.html").write_text(render_blog_index(manifest_posts), encoding="utf-8")
    (BLOG_DIR / "manifest.json").write_text(
        json.dumps({"generated_at": datetime.now().isoformat(), "posts": manifest_posts}, indent=2),
        encoding="utf-8",
    )
    return BLOG_DIR


if __name__ == "__main__":
    out = generate()
    print(f"Generated {len(ARTICLES)} articles in {out}")
