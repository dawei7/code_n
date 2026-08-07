import json
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

total_questions = len(questions)
found_editorials = 0
found_placeholders = 0
missing_files = []
empty_files = []
iframe_remnants = []

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    editorial_path = LEETCODE_ROOT / folder_name / "reference" / "editorial.md"
    
    if not editorial_path.is_file():
        missing_files.append(folder_name)
        continue
    
    content = editorial_path.read_text(encoding="utf-8")
    if not content.strip():
        empty_files.append(folder_name)
        continue
        
    if "An official LeetCode editorial is not available for this problem" in content:
        found_placeholders += 1
    else:
        found_editorials += 1
        if "playground" in content and "iframe" in content:
            iframe_remnants.append(folder_name)

print("=== EDITORIALS AUDIT REPORT ===")
print(f"Total problems in index: {total_questions}")
print(f"Editorial files present: {found_editorials + found_placeholders}/{total_questions}")
print(f"  - Official Editorials (with code conversion): {found_editorials}")
print(f"  - Editorial Placeholders: {found_placeholders}")
print(f"Missing files: {len(missing_files)}")
print(f"Empty files: {len(empty_files)}")
print(f"Unconverted Playground IFrames: {len(iframe_remnants)}")
