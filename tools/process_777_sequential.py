"""Sequential problem-by-problem campaign worker for 777_problems.txt."""

import json
import hashlib
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
    for line in lines[1:]:
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

    unverified = []
    verified = []

    for fid, name in target_problems:
        pkg = package_map.get(fid)
        if not pkg:
            continue
        res = validate_source_fidelity(pkg)
        if res.status == "verified":
            verified.append((fid, name, pkg))
        else:
            unverified.append((fid, name, pkg, res.errors))

    print(f"777 Campaign Status: {len(verified)} Verified | {len(unverified)} Remaining")
    if unverified:
        next_fid, next_name, next_pkg, errs = unverified[0]
        print(f"\nNext sequential target: ID {next_fid:04d} - {next_name} ({next_pkg.name})")

if __name__ == "__main__":
    main()
