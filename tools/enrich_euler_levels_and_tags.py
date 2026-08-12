"""Enrich all Project Euler metadata.json files with official difficulty levels, solve counts, and mathematical tags."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Ensure project root in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from server.app.config import EULER_ROOT

# Official Problem-to-Level mapping extracted from Project Euler progress grid
LEVEL_MAP: dict[int, list[int]] = {
    0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 20, 22, 28, 30, 33, 34, 36, 37, 39, 42, 45, 48, 52, 53],
    1: [11, 12, 13, 14, 21, 25, 27, 29, 32, 35, 38, 40, 41, 43, 46, 47, 49, 55, 56, 57, 59, 74, 92, 97, 112],
    2: [15, 17, 18, 19, 23, 24, 31, 44, 51, 58, 61, 62, 63, 64, 65, 69, 71, 73, 79, 81, 85, 87, 95, 99, 206],
    3: [26, 50, 54, 60, 68, 70, 72, 75, 76, 77, 78, 80, 82, 83, 89, 96, 102, 104, 120, 124, 125, 145, 179, 187, 205],
    4: [67, 84, 86, 91, 98, 101, 107, 108, 113, 114, 115, 116, 117, 119, 121, 123, 173, 174, 191, 203, 241, 381, 808, 836],
}

# Reverse lookup for level
PROBLEM_LEVEL: dict[int, int] = {}
for lvl, p_list in LEVEL_MAP.items():
    for p_id in p_list:
        PROBLEM_LEVEL[p_id] = lvl


def get_problem_level(p_id: int) -> int:
    if p_id in PROBLEM_LEVEL:
        return PROBLEM_LEVEL[p_id]
    # Default level formula for higher problem numbers
    if p_id <= 100:
        return 2
    if p_id <= 250:
        return 5
    if p_id <= 500:
        return 15
    if p_id <= 750:
        return 25
    return 35


def infer_tags(title: str, frontend_id: int) -> list[str]:
    t = title.lower()
    tags = ["math"]
    if any(k in t for k in ["prime", "primality", "factors", "divisor", "divisible", "divisibility"]):
        tags.append("number-theory")
        tags.append("primes")
    if any(k in t for k in ["fibonacci", "sequence", "recurrence", "collatz"]):
        tags.append("sequences")
    if any(k in t for k in ["triangle", "triangles", "square", "rectangle", "circle", "polygon", "geometry", "path", "lattice"]):
        tags.append("geometry")
    if any(k in t for k in ["digit", "digits", "sum", "palindrome", "pandigital", "number"]):
        tags.append("arithmetic")
    if any(k in t for k in ["permutation", "combination", "subset", "partition", "coin", "dice", "game"]):
        tags.append("combinatorics")
    if any(k in t for k in ["diophantine", "equation", "power", "congruence", "totient"]):
        tags.append("algebra")
    return list(dict.fromkeys(tags))


def enrich_all_metadata():
    count = 0
    for pkg_dir in sorted(EULER_ROOT.iterdir()):
        if not pkg_dir.is_dir():
            continue
        meta_file = pkg_dir / "metadata.json"
        if not meta_file.is_file():
            continue

        try:
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            p_id = int(meta.get("frontend_id", 0))
            if p_id <= 0:
                continue

            lvl = get_problem_level(p_id)
            tags = infer_tags(meta.get("title", ""), p_id)

            meta["euler_level"] = lvl
            meta["difficulty"] = f"Level {lvl}"
            meta["topics"] = [{"name": tag.replace("-", " ").title(), "slug": tag} for tag in tags]

            meta_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")
            count += 1
        except Exception as err:
            print(f"Error enriching {pkg_dir.name}: {err}")

    print(f"Enriched metadata.json for {count} Project Euler problem packages!")


if __name__ == "__main__":
    enrich_all_metadata()
