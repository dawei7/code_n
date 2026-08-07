import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"

sql_files_audited = 0
sql_files_fixed = 0

ifnull_count = 0
group_concat_count = 0

for pkg_dir in LEETCODE_ROOT.iterdir():
    if not pkg_dir.is_dir() or pkg_dir.name.startswith("_"):
        continue

    optimal_dir = pkg_dir / "variants" / "optimal"
    if not optimal_dir.is_dir():
        continue

    for sql_file in optimal_dir.glob("*.sql"):
        sql_files_audited += 1
        content = sql_file.read_text(encoding="utf-8", errors="ignore")
        orig = content

        if re.search(r"\bIFNULL\b", content, re.IGNORECASE):
            ifnull_count += 1
        if re.search(r"\bGROUP_CONCAT\b", content, re.IGNORECASE):
            group_concat_count += 1

        # Replace IFNULL with COALESCE for PostgreSQL / PGlite compatibility
        content = re.sub(r"\bIFNULL\b", "COALESCE", content, flags=re.IGNORECASE)

        # Replace GROUP_CONCAT(x, y) or GROUP_CONCAT(x) with STRING_AGG
        content = re.sub(r"\bGROUP_CONCAT\s*\(([^,)]+),\s*([^)]+)\)", r"STRING_AGG(\1, \2)", content, flags=re.IGNORECASE)
        content = re.sub(r"\bGROUP_CONCAT\s*\(([^)]+)\)", r"STRING_AGG(\1, ',')", content, flags=re.IGNORECASE)

        if content != orig:
            sql_file.write_text(content, encoding="utf-8")
            sql_files_fixed += 1

print(f"Optimal SQL files audited: {sql_files_audited}")
print(f"Files with IFNULL: {ifnull_count}")
print(f"Files with GROUP_CONCAT: {group_concat_count}")
print(f"Optimal SQL files updated to PostgreSQL standard: {sql_files_fixed}")
