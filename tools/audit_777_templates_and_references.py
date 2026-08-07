"""Audit template and reference completeness across all 777 target problems."""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

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

    sql_count = 0
    py_count = 0
    missing_template = []
    sql_without_postgres = []

    for fid, name in target_problems:
        pkg = package_map.get(fid)
        if not pkg:
            continue
        meta_file = pkg / "metadata.json"
        meta = json.loads(meta_file.read_text(encoding="utf-8")) if meta_file.is_file() else {}
        category = meta.get("category", "")
        
        has_py_tmpl = (pkg / "template.py").is_file()
        has_sql_tmpl = (pkg / "template.sql").is_file()

        if category == "database" or "sql" in name.lower():
            sql_count += 1
            if not has_sql_tmpl:
                sql_without_postgres.append((fid, name, pkg.name))
        else:
            py_count += 1
            if not has_py_tmpl:
                missing_template.append((fid, name, pkg.name))

    print(f"Total SQL problems: {sql_count} (SQL without template.sql: {len(sql_without_postgres)})")
    print(f"Total Python problems: {py_count} (Missing template.py: {len(missing_template)})")

    if sql_without_postgres:
        print("\nSQL problems needing PostgreSQL template.sql:")
        for item in sql_without_postgres[:10]:
            print(f"  ID {item[0]:04d}: {item[1]} -> {item[2]}")

if __name__ == "__main__":
    main()
