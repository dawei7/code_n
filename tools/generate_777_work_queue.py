"""Generate work queue for 777 problems campaign."""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tools.leetcode_source_fidelity import validate_source_fidelity

LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
PROBLEMS_TXT = REPO_ROOT / "777_problems.txt"
QUEUE_OUTPUT = LEETCODE_ROOT / "_reports" / "_777_work_queue.json"

def load_777_problems():
    problems = []
    with open(PROBLEMS_TXT, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[1:]: # skip header
        line = line.strip()
        if not line:
            continue
        parts = line.split(",", 1)
        if len(parts) >= 2:
            fid = int(parts[0].strip())
            name = parts[1].strip()
            problems.append((fid, name))
    return problems

def main():
    target_problems = load_777_problems()
    
    package_map = {}
    for p in LEETCODE_ROOT.iterdir():
        if p.is_dir() and (p / "metadata.json").is_file():
            m = re.match(r"^(\d+)_", p.name)
            if m:
                fid = int(m.group(1))
                package_map[fid] = p

    invalid_items = []
    verified_items = []

    for fid, name in target_problems:
        pkg = package_map.get(fid)
        if not pkg:
            continue
        metadata_file = pkg / "metadata.json"
        metadata = json.loads(metadata_file.read_text(encoding="utf-8")) if metadata_file.is_file() else {}
        slug = metadata.get("slug") or metadata.get("title_slug") or ""
        category = metadata.get("category", "")
        res = validate_source_fidelity(pkg)
        item = {
            "frontend_id": fid,
            "name": name,
            "package_path": str(pkg.relative_to(REPO_ROOT)).replace("\\", "/"),
            "slug": slug,
            "category": category,
            "status": res.status,
            "errors": list(res.errors),
        }
        if res.status == "verified":
            verified_items.append(item)
        else:
            invalid_items.append(item)

    queue_data = {
        "total_targets": len(target_problems),
        "verified_count": len(verified_items),
        "queue_count": len(invalid_items),
        "queue": invalid_items,
    }

    QUEUE_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_OUTPUT.write_text(json.dumps(queue_data, indent=2), encoding="utf-8")
    print(f"Generated {QUEUE_OUTPUT}")
    print(f"Verified: {len(verified_items)} | Needs Work: {len(invalid_items)}")

if __name__ == "__main__":
    main()
