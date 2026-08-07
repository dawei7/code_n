import json
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

deleted_candidates = 0
moved_solutions = 0
updated_submissions = 0

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    pkg_dir = LEETCODE_ROOT / folder_name
    if not pkg_dir.is_dir():
        continue

    # 1. Delete all candidate files
    for candidate_file in pkg_dir.rglob("candidate.*"):
        if candidate_file.is_file():
            candidate_file.unlink()
            deleted_candidates += 1

    # 2. Move solution files from variants/<variant>/solutions/solution.* to variants/<variant>/solution.*
    variants_dir = pkg_dir / "variants"
    if variants_dir.is_dir():
        for variant_dir in variants_dir.iterdir():
            if not variant_dir.is_dir():
                continue

            solutions_sub_dir = variant_dir / "solutions"
            if solutions_sub_dir.is_dir():
                for sol_file in list(solutions_sub_dir.iterdir()):
                    if sol_file.is_file():
                        target_file = variant_dir / sol_file.name
                        shutil.move(str(sol_file), str(target_file))
                        moved_solutions += 1

                # Clean up empty solutions/ directory
                try:
                    solutions_sub_dir.rmdir()
                except OSError:
                    pass

    # 3. Update submission.json files to point to "source": "solution.<ext>"
    for sub_file in pkg_dir.rglob("submission.json"):
        text = sub_file.read_text(encoding="utf-8")
        new_text = text.replace('"source": "solutions/solution.', '"source": "solution.')
        new_text = new_text.replace('"source": "solutions/leetcode.', '"source": "solution.')
        if new_text != text:
            sub_file.write_text(new_text, encoding="utf-8")
            updated_submissions += 1

print(f"Deleted candidate files: {deleted_candidates}")
print(f"Moved solution files to variant parent: {moved_solutions}")
print(f"Updated submission.json files: {updated_submissions}")
