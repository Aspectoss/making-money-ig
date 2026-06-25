#!/usr/bin/env python3
"""Generate faceless Instagram reel scripts, captions, and a posting calendar."""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).parent
CONFIG_PATH = ROOT / "config.json"
OUTPUT_DIR = ROOT / "content"


REEL_TOPICS = [
    {
        "hook": "Stop doing this with your paycheck.",
        "points": [
            "Most people pay bills first, then spend, then save whatever is left.",
            "Flip it: save or invest a fixed amount the day you get paid.",
            "Even 10% compounds faster than random leftovers at month end.",
        ],
        "cta": "Follow for one money fix every day.",
        "on_screen": ["pay yourself first", "save on payday", "not what's left over"],
    },
    {
        "hook": "This side hustle needs zero followers to start.",
        "points": [
            "Local businesses need short video ads but do not know how to edit.",
            "Offer 3 reels for $150 using stock clips and captions.",
            "Walk in with a sample reel for their shop. One yes pays for the week.",
        ],
        "cta": "Comment HUSTLE and I'll drop the outreach script.",
        "on_screen": ["$150 for 3 reels", "zero followers needed", "local businesses"],
    },
    {
        "hook": "The 24-hour rule that killed my impulse spending.",
        "points": [
            "Add everything you want to a cart or saved list.",
            "If you still want it after 24 hours, buy it.",
            "Most impulse buys die overnight. Your bank account notices.",
        ],
        "cta": "Save this before your next Target run.",
        "on_screen": ["24-hour rule", "impulse spending fix", "wait before you buy"],
    },
    {
        "hook": "You're losing money on subscriptions you forgot exist.",
        "points": [
            "Check your bank statement for recurring charges right now.",
            "Cancel anything you have not used in 30 days.",
            "The average person wastes $200+ a year on zombie subscriptions.",
        ],
        "cta": "Share this with someone who needs a subscription audit.",
        "on_screen": ["subscription audit", "$200/year wasted", "cancel unused"],
    },
    {
        "hook": "How to turn one skill into $500 this month.",
        "points": [
            "Pick one thing you already do: writing, editing, organizing, Excel.",
            "Post one before/after or result on Instagram and Facebook groups.",
            "Charge $25-50 for a small fixed task. Ten clients beats one big client early.",
        ],
        "cta": "Follow for the weekly side hustle breakdown.",
        "on_screen": ["$500 this month", "sell a skill", "10 small clients"],
    },
    {
        "hook": "Rich people do not budget like you think.",
        "points": [
            "They track three numbers: income, fixed costs, and investment rate.",
            "Everything else is flexible spending, not guilt.",
            "Simplify your budget to those three and you will actually stick to it.",
        ],
        "cta": "Save this for your next budget reset.",
        "on_screen": ["3-number budget", "income / fixed / invest", "skip the spreadsheet guilt"],
    },
    {
        "hook": "The free tool that replaced my financial advisor.",
        "points": [
            "A simple net worth tracker: assets minus debts, updated monthly.",
            "You cannot improve what you do not measure.",
            "Google Sheets template is enough. Fancy apps are optional.",
        ],
        "cta": "Link in bio for the free tracker template.",
        "on_screen": ["net worth tracker", "assets - debts", "update monthly"],
    },
    {
        "hook": "If you make under $60k, do this with your tax refund.",
        "points": [
            "Do not treat it like bonus spending money.",
            "Split 50% emergency fund, 30% debt, 20% fun.",
            "One disciplined refund can break the paycheck-to-paycheck cycle.",
        ],
        "cta": "Follow before tax season sneaks up.",
        "on_screen": ["50/30/20 refund split", "emergency fund first", "not a shopping spree"],
    },
    {
        "hook": "Nobody talks about this Amazon return trick.",
        "points": [
            "Check return windows before buying seasonal items.",
            "Price track big purchases with free browser tools.",
            "Returning or repricing one item a month adds up over a year.",
        ],
        "cta": "Save this for your next online order.",
        "on_screen": ["return windows", "price tracking", "small wins add up"],
    },
    {
        "hook": "I made my first $100 online in 48 hours doing this.",
        "points": [
            "Listed a Notion or Canva template on Gumroad for $9.",
            "Posted the problem it solves in 3 Facebook and Reddit groups.",
            "Eleven sales at $9 beats waiting for a perfect product.",
        ],
        "cta": "Comment TEMPLATE if you want the listing checklist.",
        "on_screen": ["$9 digital product", "Gumroad", "48 hours"],
    },
]


def load_config() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def pick_hashtags(config: dict, index: int) -> list[str]:
    sets = config["content"]["hashtag_sets"]
    return sets[index % len(sets)]


def format_script(topic: dict) -> str:
    lines = [topic["hook"], ""]
    for i, point in enumerate(topic["points"], 1):
        lines.append(f"{i}. {point}")
    lines.extend(["", f"CTA: {topic['cta']}"])
    return "\n".join(lines)


def format_caption(topic: dict, hashtags: list[str]) -> str:
    body = "\n".join(topic["points"])
    tags = " ".join(hashtags)
    return f"{topic['hook']}\n\n{body}\n\n{topic['cta']}\n\n{tags}"


def build_calendar(start: datetime, count: int, times: list[str]) -> list[dict]:
    schedule = []
    for i in range(count):
        day = start + timedelta(days=i)
        schedule.append(
            {
                "date": day.strftime("%Y-%m-%d"),
                "weekday": day.strftime("%A"),
                "post_time": times[i % len(times)],
            }
        )
    return schedule


def generate_week(config: dict | None = None) -> Path:
    config = config or load_config()
    count = config["content"]["posts_per_week"]
    topics = random.sample(REEL_TOPICS, k=min(count, len(REEL_TOPICS)))
    calendar = build_calendar(
        datetime.now().replace(hour=0, minute=0, second=0, microsecond=0),
        count,
        config["content"]["best_post_times"],
    )

    stamp = datetime.now().strftime("%Y-%m-%d")
    week_dir = OUTPUT_DIR / f"week-{stamp}"
    week_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "niche": config["account"]["niche"],
        "posts": [],
    }

    for i, (slot, topic) in enumerate(zip(calendar, topics), 1):
        post_id = f"day-{i:02d}"
        post_dir = week_dir / post_id
        post_dir.mkdir(exist_ok=True)

        hashtags = pick_hashtags(config, i - 1)
        script = format_script(topic)
        caption = format_caption(topic, hashtags)

        (post_dir / "script.txt").write_text(script, encoding="utf-8")
        (post_dir / "caption.txt").write_text(caption, encoding="utf-8")
        (post_dir / "on-screen-text.txt").write_text(
            "\n".join(topic["on_screen"]), encoding="utf-8"
        )
        (post_dir / "production-notes.txt").write_text(
            "\n".join(
                [
                    f"Post: {slot['weekday']} {slot['date']} at {slot['post_time']}",
                    "",
                    "How to make this reel (15-30 sec):",
                    "1. Open CapCut or Instagram Reels.",
                    "2. Use stock b-roll: typing on laptop, wallet, calendar, coffee shop.",
                    "3. Add bold on-screen text from on-screen-text.txt (one line every 3-5 sec).",
                    "4. Use a trending lo-fi or motivational audio (check Reels audio tab).",
                    "5. Paste caption.txt when posting.",
                    "",
                    "Monetization:",
                    "- Pin a comment: 'Free guide in bio'",
                    "- Link in bio page captures emails and affiliate clicks",
                ]
            ),
            encoding="utf-8",
        )

        manifest["posts"].append(
            {
                "id": post_id,
                "schedule": slot,
                "hook": topic["hook"],
                "folder": str(post_dir.relative_to(ROOT)),
            }
        )

    (week_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    (week_dir / "CHECKLIST.md").write_text(
        "\n".join(
            [
                "# This Week's Posting Checklist",
                "",
                "Do these once:",
                "- [ ] Create Instagram account (business profile)",
                "- [ ] Deploy bio-page/index.html (Netlify drop is free)",
                "- [ ] Replace affiliate links in config.json and bio page",
                "- [ ] Upload profile pic (Canva: bold text logo works)",
                "",
                "Do these daily:",
            ]
            + [
                f"- [ ] {p['schedule']['weekday']} {p['schedule']['post_time']}: {p['hook']} (`{p['folder']}`)"
                for p in manifest["posts"]
            ]
            + [
                "",
                "Money path:",
                "1. Week 1-2: post daily, reply to every comment",
                "2. Week 3: add free PDF lead magnet, link in bio",
                "3. Week 4+: affiliate links in bio, pitch $9 template or guide",
                "4. Month 2+: brand DMs when you hit 1k+ followers",
            ]
        ),
        encoding="utf-8",
    )

    return week_dir


if __name__ == "__main__":
    path = generate_week()
    print(f"Generated content pack: {path}")
    print(f"Open {path / 'CHECKLIST.md'} and start with Day 01.")
