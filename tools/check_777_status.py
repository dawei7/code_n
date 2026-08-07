"""Check strict validation status of all 777 problems in 777_problems.txt using validate_source_fidelity."""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tools.leetcode_source_fidelity import validate_source_fidelity

LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
PROBLEMS_TXT = REPO_ROOT / "777_problems.txt"

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
    print(f"Total problems in 777_problems.txt: {len(target_problems)}")
    
    package_map = {}
    for p in LEETCODE_ROOT.iterdir():
        if p.is_dir() and (p / "metadata.json").is_file():
            m = re.match(r"^(\d+)_", p.name)
            if m:
                fid = int(m.group(1))
                package_map[fid] = p

    missing = []
    invalid = []
    unverified = []
    verified = []

    for fid, name in target_problems:
        pkg = package_map.get(fid)
        if not pkg:
            missing.append((fid, name))
            continue
        res = validate_source_fidelity(pkg)
        if res.status == "verified":
            verified.append((fid, name, pkg.name))
        elif res.status == "invalid":
            invalid.append((fid, name, pkg.name, res.errors))
        else:
            unverified.append((fid, name, pkg.name))

    print(f"Verified: {len(verified)}")
    print(f"Invalid: {len(invalid)}")
    print(f"Unverified: {len(unverified)}")
    print(f"Missing: {len(missing)}")

    if invalid or unverified:
        print("\nFirst 15 problematic packages:")
        for item in (invalid + unverified)[:15]:
            fid, name, pkg_name = item[0], item[1], item[2]
            errs = item[3] if len(item) > 3 else ()
            print(f"  ID {fid:04d}: {name} -> {pkg_name} | Errors: {errs}")

if __name__ == "__main__":
    main()
