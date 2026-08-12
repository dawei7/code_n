"""Scrape exact official Project Euler tags and difficulty levels for all 1,007 problems using authenticated CDP cookies."""

from __future__ import annotations

import asyncio
import json
import re
import sys
import time
import urllib.request
import websockets
from pathlib import Path

# Ensure project root in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from server.app.config import EULER_ROOT
from tools.build_euler_index import build_euler_index


def get_browser_ws_url() -> str:
    with urllib.request.urlopen("http://127.0.0.1:9222/json/version") as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data["webSocketDebuggerUrl"]


async def fetch_cdp_cookies() -> dict[str, str]:
    ws_url = get_browser_ws_url()
    async with websockets.connect(ws_url) as ws:
        req = {"id": 1, "method": "Storage.getCookies"}
        await ws.send(json.dumps(req))
        resp = await ws.recv()
        data = json.loads(resp)
        cookies = {}
        for c in data.get("result", {}).get("cookies", []):
            if "projecteuler.net" in c.get("domain", ""):
                cookies[c["name"]] = c["value"]
        return cookies


def fetch_problem_page(p_id: int, cookie_header: str) -> str:
    url = f"https://projecteuler.net/problem={p_id}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Cookie": cookie_header,
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as err:
        print(f"Error fetching problem {p_id}: {err}")
        return ""


def parse_tags_and_level(html: str) -> tuple[list[str], int, str]:
    # Extract tags
    # <form class="csrf_form" method="post" action="search_tags=slug"><input type="submit" value="slug">
    tag_matches = re.findall(r'action="search_tags=([^"]+)"', html)
    tags = []
    for t in tag_matches:
        t_clean = t.strip()
        # Ignore numeric problem match form value
        if t_clean and not t_clean.isdigit() and t_clean not in tags:
            tags.append(t_clean)

    # Extract Level
    # [Level 0] or [Level 15]
    level = 0
    diff_label = "Level 0"
    level_match = re.search(r"\[Level\s+(\d+)\]", html)
    if level_match:
        level = int(level_match.group(1))
        diff_label = f"Level {level}"

    return tags, level, diff_label


def main():
    print("Fetching authenticated Chrome cookies via CDP...")
    cookies = asyncio.run(fetch_cdp_cookies())
    if not cookies:
        print("Error: No Project Euler cookies found in Chrome CDP!")
        return

    cookie_header = "; ".join(f"{k}={v}" for k, v in cookies.items())
    print(f"Authenticated with {len(cookies)} cookies.")
    print("Scraping official tags and difficulty levels for all 1,007 problems...")

    success_count = 0
    for p_id in range(1, 1008):
        num_str = str(p_id).zfill(4)
        matches = list(EULER_ROOT.glob(f"{num_str}_*"))
        if not matches:
            continue
        pkg_dir = matches[0]
        meta_file = pkg_dir / "metadata.json"
        if not meta_file.is_file():
            continue

        html = fetch_problem_page(p_id, cookie_header)
        if not html:
            continue

        tags, level, diff_label = parse_tags_and_level(html)

        try:
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            meta["euler_level"] = level
            meta["difficulty"] = diff_label
            meta["topics"] = [
                {"name": t.replace("-", " ").title(), "slug": t}
                for t in tags
            ]
            meta_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")
            success_count += 1
        except Exception as err:
            print(f"Error updating metadata for problem {p_id}: {err}")

        if p_id % 50 == 0 or p_id == 1007:
            print(f"Processed {p_id}/1007 problems... (Latest problem {p_id}: {diff_label}, tags: {tags})")

        time.sleep(0.03)

    print(f"\nSuccessfully updated official tags and levels for {success_count} Project Euler problem packages!")
    print("Rebuilding dsa/euler/index.json...")
    build_euler_index()


if __name__ == "__main__":
    main()
