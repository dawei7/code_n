"""Fetch exact official Project Euler tags for all problems using authenticated CDP cookies."""

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

OFFICIAL_TAG_SLUGS = [
    "analytic-geometry", "area", "arithmetic-operator", "arithmetic-progression", "asymptotics",
    "binary-equation", "binary-operator", "binomial-coefficient", "bisection", "calendar",
    "cards", "chess", "chinese-remainder-theorem", "circle", "circumcircle",
    "collatz-sequence", "colouring", "combinatorics", "complex-number", "connectivity",
    "continued-fraction", "convexity", "coordinate-system", "coprime-numbers", "cryptography",
    "cube-number", "cube-root", "cycle", "decimal-representation", "digit-manipulation",
    "digit-sum", "diophantine-equation", "dirichlet-convolution", "divisibility", "divisor-count",
    "divisor-sum", "ellipse", "euclidean-algorithm", "expectation", "exponentiation-by-squaring",
    "factorial", "factorisation", "fibonacci-number", "figurate-number", "fraction",
    "game", "gaussian-integer", "gcd", "geometric-progression", "geometry",
    "golden-ratio", "graph", "grid-pattern", "harmonic-number", "herons-formula",
    "hexagon", "hexagonal-lattice", "huffman-code", "incircle", "interpolation",
    "iterated-polynomial", "iterative-method", "lambda-calculus", "large-numbers", "lattice",
    "lattice-point-counting", "lcm", "lexicographic-ordering", "linear-recurrence", "longest-path",
    "lucas-number", "markov-chain", "matrix", "median-number", "mobius-function",
    "modular-arithmetic", "modular-inverse", "modular-root", "multiplicative-function", "multiplicative-order",
    "multiset", "nim", "non-discrete", "number-base", "optimisation",
    "orthocentre", "p-adic-number", "p-adic-valuation", "packing", "palindrome",
    "pandigital", "parametrisation", "partisan-game", "partition", "path-finding",
    "pattern-matching", "pells-equation", "periodicity", "permutation", "physics",
    "polygon", "polynomial", "popcount", "power", "prime-counting",
    "prime-number", "probability", "pythagorean-theorem", "pythagorean-triple", "quadratic-equation",
    "random-walk", "recurring-decimal", "recursion", "roman-numeral", "sequence",
    "sequence-generator", "sequence-summation", "shortest-path", "smooth-number", "sorting",
    "spanning-tree", "sphere", "square", "square-number", "square-root",
    "squarefree-number", "state-machine", "stern-brocot-tree", "sublinear-number-theoretic-summation", "subset",
    "substring", "sum-of-powers", "sum-of-squares", "tangency", "thue-morse-sequence",
    "tiling", "totient-function", "travelling-salesman", "tree", "triangle",
    "triangle-median", "triangle-number", "trigonometry", "volume", "word-problem",
    "xor", "young-tableau", "zeckendorf-representation"
]


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


def fetch_url_with_cookies(url: str, cookie_header: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Cookie": cookie_header,
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as err:
        return ""


def fetch_tag_problems(tag_slug: str, cookie_header: str) -> list[int]:
    problem_ids: list[int] = []
    page = 1
    while True:
        url = f"https://projecteuler.net/tag={tag_slug}" if page == 1 else f"https://projecteuler.net/tag={tag_slug};page={page}"
        html = fetch_url_with_cookies(url, cookie_header)
        matches = re.findall(r'href="problem=(\d+)"', html)
        if not matches:
            break
        added_new = False
        for m in matches:
            p_id = int(m)
            if p_id not in problem_ids:
                problem_ids.append(p_id)
                added_new = True

        if not added_new:
            break

        # Check if paginated
        if f"tag={tag_slug};page={page + 1}" in html:
            page += 1
            time.sleep(0.02)
        else:
            break
    return problem_ids


def main():
    print("Fetching authenticated Chrome cookies via CDP...")
    cookies = asyncio.run(fetch_cdp_cookies())
    if not cookies:
        print("Error: No Project Euler cookies found in Chrome CDP!")
        return

    cookie_header = "; ".join(f"{k}={v}" for k, v in cookies.items())
    print(f"Authenticated with {len(cookies)} cookies.")
    print(f"Fetching official problem lists for all {len(OFFICIAL_TAG_SLUGS)} Project Euler tags...")

    problem_tags_map: dict[int, list[str]] = {}
    for idx, tag_slug in enumerate(OFFICIAL_TAG_SLUGS, 1):
        p_ids = fetch_tag_problems(tag_slug, cookie_header)
        for p_id in p_ids:
            problem_tags_map.setdefault(p_id, []).append(tag_slug)
        if idx % 20 == 0 or idx == len(OFFICIAL_TAG_SLUGS):
            print(f"Processed {idx}/{len(OFFICIAL_TAG_SLUGS)} tags... (Found {len(problem_tags_map)} tagged problems so far)")
        time.sleep(0.02)

    print(f"\nMapped official tags for {len(problem_tags_map)} problems!")

    # Update metadata.json files with preserved level and new official tags
    updated_count = 0
    for pkg_dir in sorted(EULER_ROOT.iterdir()):
        if not pkg_dir.is_dir():
            continue
        meta_file = pkg_dir / "metadata.json"
        if not meta_file.is_file():
            continue

        try:
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            p_id = int(meta.get("frontend_id", 0))
            tag_slugs = problem_tags_map.get(p_id, [])
            meta["topics"] = [
                {"name": slug.replace("-", " ").title(), "slug": slug}
                for slug in tag_slugs
            ]
            meta_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")
            updated_count += 1
        except Exception as err:
            print(f"Error updating metadata for {pkg_dir.name}: {err}")

    print(f"Successfully updated official Project Euler tags in metadata.json for {updated_count} problems!")
    print("Rebuilding dsa/euler/index.json...")
    build_euler_index()


if __name__ == "__main__":
    main()
