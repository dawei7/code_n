import json
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

updated_manifests = 0

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    manifest_path = LEETCODE_ROOT / folder_name / "solution_variants.json"
    if manifest_path.is_file():
        text = manifest_path.read_text(encoding="utf-8")
        new_text = text.replace("leetcode.py", "solution.py")
        new_text = new_text.replace("leetcode.js", "solution.js")
        new_text = new_text.replace("leetcode_sqlite.sql", "solution.sql")
        new_text = new_text.replace("leetcode.sql", "solution.sql")
        new_text = new_text.replace("leetcode.sh", "solution.sh")
        new_text = new_text.replace("solve.py", "solution.py")

        if new_text != text:
            manifest_path.write_text(new_text, encoding="utf-8")
            updated_manifests += 1

print(f"Updated solution_variants.json manifests: {updated_manifests}")
