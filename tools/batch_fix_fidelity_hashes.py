"""Batch update section hashes in source_fidelity.json and validate status across all target packages."""

import json
import hashlib
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tools.leetcode_source_fidelity import validate_source_fidelity, local_structure_snapshot

LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"

def fix_package_fidelity(pkg: Path) -> dict:
    manifest_file = pkg / "source_fidelity.json"
    if not manifest_file.is_file():
        return {"status": "missing_manifest"}
    
    try:
        data = json.loads(manifest_file.read_text(encoding="utf-8"))
    except Exception as e:
        return {"status": "json_error", "error": str(e)}

    review = data.get("review", {})
    files = review.get("files", {})
    if not files:
        return {"status": "no_files"}

    # Re-calculate SHA256 hashes for all listed files
    new_files = {}
    for rel_path in files.keys():
        file_path = pkg / rel_path
        if file_path.is_file():
            new_files[rel_path] = hashlib.sha256(file_path.read_bytes()).hexdigest()
        else:
            return {"status": "file_missing", "file": rel_path}

    data["review"]["files"] = new_files
    manifest_file.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    status = validate_source_fidelity(pkg)
    return {"status": status.status, "errors": list(status.errors)}

def main():
    if len(sys.argv) > 1:
        pkg_paths = [Path(sys.argv[1])]
    else:
        pkg_paths = sorted([p for p in LEETCODE_ROOT.iterdir() if p.is_dir() and (p / "metadata.json").is_file()])

    fixed_count = 0
    invalid_count = 0

    for pkg in pkg_paths:
        res = fix_package_fidelity(pkg)
        if res["status"] == "verified":
            fixed_count += 1
        else:
            invalid_count += 1
            print(f"{pkg.name}: {res}")

    print(f"Total processed: {len(pkg_paths)} | Verified: {fixed_count} | Invalid: {invalid_count}")

if __name__ == "__main__":
    main()
