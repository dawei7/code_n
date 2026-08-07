import json
import re
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

unbalanced_desc = []
unbalanced_ed = []

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"

    desc_file = ref_dir / "description.md"
    if desc_file.is_file():
        content = desc_file.read_text(encoding="utf-8")
        # Count occurrence of ```
        fences = len(re.findall(r'```', content))
        if fences % 2 != 0:
            unbalanced_desc.append((folder_name, fences))

    ed_file = ref_dir / "editorial.md"
    ed_file_raw = ref_dir / "raw" / "raw_editorial.md"
    if ed_file.is_file():
        content = ed_file.read_text(encoding="utf-8")
        fences = len(re.findall(r'```', content))
        if fences % 2 != 0:
            unbalanced_ed.append((folder_name, fences))

print("=== CODE BLOCK BALANCE AUDIT ===")
print(f"Total problems audited: {len(questions)}")
print(f"Unbalanced descriptions found: {len(unbalanced_desc)}")
print(f"Unbalanced editorials found: {len(unbalanced_ed)}")

if unbalanced_desc:
    print("\nSample unbalanced descriptions:")
    for f, c in unbalanced_desc[:10]:
        print(f"  {f}: {c} ``` occurrences")

if unbalanced_ed:
    print("\nSample unbalanced editorials:")
    for f, c in unbalanced_ed[:10]:
        print(f"  {f}: {c} ``` occurrences")
