"""Apply the exact scraped official Project Euler tags to all metadata.json packages.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

# Ensure project root in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

TAG_MAPPING_PATH = Path("scratch/euler_official_tags_mapping.json")
if not TAG_MAPPING_PATH.is_file():
    print("Error: scratch/euler_official_tags_mapping.json not found.")
    sys.exit(1)

mapping_data = json.loads(TAG_MAPPING_PATH.read_text(encoding="utf-8"))
p2t = mapping_data["problemToTags"]

# Proper title casing for math terms
SPECIAL_CASING = {
    "gcd": "GCD",
    "chinese-remainder-theorem": "Chinese Remainder Theorem",
    "huffman-code": "Huffman Code",
    "herons-formula": "Heron's Formula",
    "collatz-sequence": "Collatz Sequence",
    "fibonacci-number": "Fibonacci Number",
    "gaussian-integer": "Gaussian Integer",
    "diophantine-equation": "Diophantine Equation",
    "dirichlet-convolution": "Dirichlet Convolution",
    "lucas-theorem": "Lucas' Theorem",
    "farey-sequence": "Farey Sequence",
    "pell-equation": "Pell's Equation",
    "mobius-inversion": "Möbius Inversion",
    "stern-brocot-tree": "Stern-Brocot Tree",
    "nim-game": "Nim Game",
    "wilson-theorem": "Wilson's Theorem",
    "legendre-formula": "Legendre's Formula",
    "cayley-hamilton-theorem": "Cayley-Hamilton Theorem",
}

def format_tag_name(slug: str) -> str:
    if slug in SPECIAL_CASING:
        return SPECIAL_CASING[slug]
    return slug.replace("-", " ").title()

euler_root = REPO_ROOT / "dsa" / "euler"
all_metas = sorted(euler_root.glob("*/metadata.json"))

updated_count = 0
for mpath in all_metas:
    data = json.loads(mpath.read_text(encoding="utf-8"))
    fid = str(data.get("frontend_id", "")).strip()
    
    tags = p2t.get(fid, [])
    formatted_topics = [
        {
            "name": format_tag_name(t["slug"]),
            "slug": t["slug"],
        }
        for t in tags
    ]
    
    data["topics"] = formatted_topics
    mpath.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    updated_count += 1

print(f"Updated official Project Euler tags across all {updated_count} problem metadata files.")

from tools.build_euler_index import build_euler_index
build_euler_index()
print("Rebuilt dsa/euler/index.json successfully.")
