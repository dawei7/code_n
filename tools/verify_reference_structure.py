import json
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

desc_count = 0
ed_count = 0
raw_dir_count = 0
raw_desc_count = 0
raw_ed_count = 0
raw_contract_count = 0
unexpected_items_count = 0

allowed_names = {"description.md", "editorial.md", "images", "raw"}

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"

    if not ref_dir.is_dir():
        continue

    if (ref_dir / "description.md").is_file():
        desc_count += 1
    if (ref_dir / "editorial.md").is_file():
        ed_count += 1

    raw_dir = ref_dir / "raw"
    if raw_dir.is_dir():
        raw_dir_count += 1
        if (raw_dir / "raw_description.md").is_file():
            raw_desc_count += 1
        if (raw_dir / "raw_editorial.md").is_file():
            raw_ed_count += 1
        if (raw_dir / "raw_contract.md").is_file():
            raw_contract_count += 1

    for item in ref_dir.iterdir():
        if item.name not in allowed_names:
            unexpected_items_count += 1

print("=== FINAL REFERENCE STRUCTURE AUDIT ===")
print(f"Total problems audited: {len(questions)}")
print(f"description.md present: {desc_count}/4005")
print(f"editorial.md present: {ed_count}/4005")
print(f"raw/ directory present: {raw_dir_count}/4005")
print(f"  - raw/raw_description.md present: {raw_desc_count}/4005")
print(f"  - raw/raw_editorial.md present: {raw_ed_count}/4005")
print(f"  - raw/raw_contract.md present: {raw_contract_count}/4005")
print(f"Unexpected / leftover files in reference/: {unexpected_items_count}")
