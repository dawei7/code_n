import json
import re
from pathlib import Path
from collections import Counter

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

heading_counter = Counter()

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    raw_desc = LEETCODE_ROOT / folder_name / "reference" / "raw" / "raw_description.md"
    if raw_desc.is_file():
        content = raw_desc.read_text(encoding="utf-8")
        # Find all bold or heading titles like **Title:** or ### Title
        matches = re.findall(r'^\s*(?:#+|\*\*)\s*([A-Za-z0-9_\-\s]+?):?\s*(?:\*\*|$)', content, flags=re.MULTILINE)
        for m in matches:
            clean_m = m.strip()
            if len(clean_m) < 40 and not clean_m.startswith("Input") and not clean_m.startswith("Output") and not clean_m.startswith("Explanation"):
                heading_counter[clean_m] += 1

print("=== MOST COMMON TITLES / HEADINGS IN RAW DESCRIPTIONS ===")
for title, count in heading_counter.most_common(30):
    print(f"  {title}: {count}")
