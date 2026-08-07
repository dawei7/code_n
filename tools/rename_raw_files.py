import json
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

total_questions = len(questions)
renamed_descriptions = 0
renamed_editorials = 0

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"
    
    if not ref_dir.is_dir():
        continue

    desc_file = ref_dir / "description.md"
    raw_desc_file = ref_dir / "raw_description.md"
    if desc_file.is_file():
        if raw_desc_file.is_file():
            raw_desc_file.unlink()
        desc_file.rename(raw_desc_file)
        renamed_descriptions += 1

    ed_file = ref_dir / "editorial.md"
    raw_ed_file = ref_dir / "raw_editorial.md"
    if ed_file.is_file():
        if raw_ed_file.is_file():
            raw_ed_file.unlink()
        ed_file.rename(raw_ed_file)
        renamed_editorials += 1

print("=== RENAME COMPLETED ===")
print(f"Total problems processed: {total_questions}")
print(f"Renamed description.md -> raw_description.md: {renamed_descriptions}")
print(f"Renamed editorial.md -> raw_editorial.md: {renamed_editorials}")
