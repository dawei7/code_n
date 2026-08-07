import json
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

raw_descriptions_found = 0
raw_editorials_found = 0
old_descriptions_remaining = 0
old_editorials_remaining = 0

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"

    if (ref_dir / "raw_description.md").is_file():
        raw_descriptions_found += 1
    if (ref_dir / "raw_editorial.md").is_file():
        raw_editorials_found += 1

    if (ref_dir / "description.md").is_file():
        old_descriptions_remaining += 1
    if (ref_dir / "editorial.md").is_file():
        old_editorials_remaining += 1

print("=== VERIFICATION RENAME REPORT ===")
print(f"raw_description.md present: {raw_descriptions_found}/4005")
print(f"raw_editorial.md present: {raw_editorials_found}/4005")
print(f"Old description.md remaining: {old_descriptions_remaining}")
print(f"Old editorial.md remaining: {old_editorials_remaining}")
