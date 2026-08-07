import json
import shutil
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"

def organize_package_reference(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"

    if not ref_dir.is_dir():
        return fid, slug, 0, 0

    raw_dir = ref_dir / "raw"
    raw_dir.mkdir(exist_ok=True)

    moved_count = 0
    deleted_count = 0

    # 1. Move raw_description.md -> raw/raw_description.md
    old_raw_desc = ref_dir / "raw_description.md"
    if old_raw_desc.is_file():
        target = raw_dir / "raw_description.md"
        shutil.move(str(old_raw_desc), str(target))
        moved_count += 1

    # 2. Move raw_editorial.md -> raw/raw_editorial.md
    old_raw_ed = ref_dir / "raw_editorial.md"
    if old_raw_ed.is_file():
        target = raw_dir / "raw_editorial.md"
        shutil.move(str(old_raw_ed), str(target))
        moved_count += 1

    # 3. Move contract.md / raw_contract.md -> raw/raw_contract.md
    old_contract = ref_dir / "contract.md"
    old_raw_contract = ref_dir / "raw_contract.md"
    target_contract = raw_dir / "raw_contract.md"

    if old_contract.is_file():
        shutil.move(str(old_contract), str(target_contract))
        moved_count += 1
    elif old_raw_contract.is_file():
        shutil.move(str(old_raw_contract), str(target_contract))
        moved_count += 1

    # 4. Clean up all other files in ref_dir except description.md, editorial.md, images/, raw/
    allowed_names = {"description.md", "editorial.md", "images", "raw"}

    for item in list(ref_dir.iterdir()):
        if item.name not in allowed_names:
            if item.is_file() or item.is_symlink():
                item.unlink()
                deleted_count += 1
            elif item.is_dir():
                shutil.rmtree(item)
                deleted_count += 1

    return fid, slug, moved_count, deleted_count

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]

    total = len(questions)
    print(f"Organizing reference/ into raw/ and cleaning up across {total} problems...")
    start_time = time.time()

    total_moved = 0
    total_deleted = 0
    completed = 0

    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_q = {executor.submit(organize_package_reference, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, moved, deleted = future.result()
            completed += 1
            total_moved += moved
            total_deleted += deleted

            if completed % 500 == 0 or completed == total:
                elapsed = time.time() - start_time
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Raw Files Moved: {total_moved}, Obsolete Files Deleted: {total_deleted}")

    elapsed = time.time() - start_time
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")
    print(f"Total raw files moved into reference/raw/: {total_moved}")
    print(f"Total obsolete files deleted from reference/: {total_deleted}")

if __name__ == "__main__":
    main()
