#!/usr/bin/env python3
"""Refresh the live numbers baked into the agent-trace SVGs and README.

Runs daily via .github/workflows/telemetry.yml. Fetches real stats from the
GitHub API and rewrites the tspans tagged with ids in both SVG themes, plus
the sync date in the README footer.
"""
import datetime
import json
import os
import pathlib
import re
import urllib.request

USER = "Rohith2989"
ROOT = pathlib.Path(__file__).resolve().parent.parent


def api(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_stats() -> dict:
    user = api(f"https://api.github.com/users/{USER}")
    year = datetime.date.today().year
    commits = api(
        "https://api.github.com/search/commits"
        f"?q=author:{USER}+author-date:%3E%3D{year}-01-01"
    )
    return {
        "repos": user["public_repos"],
        "commits": commits["total_count"],
        "date": datetime.date.today().isoformat(),
    }


def patch(path: pathlib.Path, replacements: list[tuple[str, str]]) -> bool:
    text = original = path.read_text()
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    if text != original:
        path.write_text(text)
        return True
    return False


def main() -> None:
    stats = fetch_stats()
    changed = False

    svg_rules = [
        (r'(id="stat-repos"[^>]*>)[^<]*(</tspan>)', rf"\g<1>{stats['repos']}\g<2>"),
        (r'(id="stat-commits"[^>]*>)[^<]*(</tspan>)', rf"\g<1>{stats['commits']}\g<2>"),
        (r'(id="telemetry-date"[^>]*>)[^<]*(</tspan>)', rf"\g<1>{stats['date']}\g<2>"),
    ]
    for theme in ["dark", "light"]:
        svg = ROOT / "assets" / f"agent-trace-{theme}.svg"
        changed |= patch(svg, svg_rules)

    readme_rules = [(r"(<!--SYNC-->)[^<]*(<!--/SYNC-->)", rf"\g<1>{stats['date']}\g<2>")]
    changed |= patch(ROOT / "README.md", readme_rules)

    print(f"stats={stats} changed={changed}")


if __name__ == "__main__":
    main()
