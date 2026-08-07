import ast
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"

py_fixed = 0
sql_fixed = 0

for pkg_dir in LEETCODE_ROOT.iterdir():
    if not pkg_dir.is_dir() or pkg_dir.name.startswith("_"):
        continue

    comp_dir = pkg_dir / "variants" / "competitive"
    if not comp_dir.is_dir():
        continue

    # 1. Fix Python competitive solutions
    for py_file in comp_dir.glob("*.py"):
        content = py_file.read_text(encoding="utf-8", errors="ignore")
        orig = content

        # Strip non-printable control characters except \n \r \t
        content = "".join(c for c in content if c in "\n\r\t" or (ord(c) >= 32 and ord(c) != 127))

        content = re.sub(r"\.iteritems\(\)", ".items()", content)
        content = re.sub(r"\.itervalues\(\)", ".values()", content)
        content = re.sub(r"\.iterkeys\(\)", ".keys()", content)
        content = re.sub(r"\bsys\.maxint\b", "sys.maxsize", content)
        content = re.sub(r"\bxrange\b", "range", content)

        if content != orig:
            py_file.write_text(content, encoding="utf-8")
            py_fixed += 1

    # 2. Fix SQL competitive solutions for PostgreSQL compatibility
    for sql_file in comp_dir.glob("*.sql"):
        content = sql_file.read_text(encoding="utf-8", errors="ignore")
        orig = content

        # Replace IFNULL with COALESCE for PostgreSQL / PGlite compatibility
        content = re.sub(r"\bIFNULL\b", "COALESCE", content, flags=re.IGNORECASE)
        # Replace GROUP_CONCAT(x, y) or GROUP_CONCAT(x) with STRING_AGG
        content = re.sub(r"\bGROUP_CONCAT\s*\(([^,)]+),\s*([^)]+)\)", r"STRING_AGG(\1, \2)", content, flags=re.IGNORECASE)
        content = re.sub(r"\bGROUP_CONCAT\s*\(([^)]+)\)", r"STRING_AGG(\1, ',')", content, flags=re.IGNORECASE)

        if content != orig:
            sql_file.write_text(content, encoding="utf-8")
            sql_fixed += 1

print(f"Python files fixed: {py_fixed}")
print(f"SQL files fixed for Postgres compatibility: {sql_fixed}")
