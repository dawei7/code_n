import json
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

updated_submissions = 0

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    pkg_dir = LEETCODE_ROOT / folder_name
    if not pkg_dir.is_dir():
        continue

    for sub_file in pkg_dir.rglob("submission.json"):
        text = sub_file.read_text(encoding="utf-8")
        new_text = text.replace("solutions/leetcode.py", "solutions/solution.py")
        new_text = new_text.replace("solutions/leetcode.js", "solutions/solution.js")
        new_text = new_text.replace("solutions/leetcode_sqlite.sql", "solutions/solution.sql")
        new_text = new_text.replace("solutions/leetcode.sql", "solutions/solution.sql")
        new_text = new_text.replace("solutions/leetcode.sh", "solutions/solution.sh")
        new_text = new_text.replace("solutions/solve.py", "solutions/solution.py")

        if new_text != text:
            sub_file.write_text(new_text, encoding="utf-8")
            updated_submissions += 1

print(f"Updated submission.json files: {updated_submissions}")
