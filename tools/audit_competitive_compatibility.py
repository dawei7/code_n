import ast
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"

py_syntax_errors = []
py2_leftovers = []
sql_dialect_warnings = []

for pkg_dir in LEETCODE_ROOT.iterdir():
    if not pkg_dir.is_dir() or pkg_dir.name.startswith("_"):
        continue

    comp_dir = pkg_dir / "variants" / "competitive"
    if not comp_dir.is_dir():
        continue

    # 1. Audit Python files
    for py_file in comp_dir.glob("*.py"):
        code = py_file.read_text(encoding="utf-8", errors="ignore")

        # AST Parse check for Python 3 validity
        try:
            ast.parse(code)
        except SyntaxError as e:
            py_syntax_errors.append((str(py_file.relative_to(REPO_ROOT)), str(e)))

        # Python 2 construct checks
        if re.search(r"\bxrange\b", code):
            py2_leftovers.append((str(py_file.relative_to(REPO_ROOT)), "xrange"))
        if re.search(r"\.iteritems\(\)", code):
            py2_leftovers.append((str(py_file.relative_to(REPO_ROOT)), ".iteritems()"))
        if re.search(r"\.itervalues\(\)", code):
            py2_leftovers.append((str(py_file.relative_to(REPO_ROOT)), ".itervalues()"))
        if re.search(r"\bsys\.maxint\b", code):
            py2_leftovers.append((str(py_file.relative_to(REPO_ROOT)), "sys.maxint"))

    # 2. Audit SQL files
    for sql_file in comp_dir.glob("*.sql"):
        code = sql_file.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"\bIFNULL\b", code, re.IGNORECASE):
            sql_dialect_warnings.append((str(sql_file.relative_to(REPO_ROOT)), "IFNULL (SQLite specific, prefer COALESCE for Postgres)"))
        if re.search(r"\bGROUP_CONCAT\b", code, re.IGNORECASE):
            sql_dialect_warnings.append((str(sql_file.relative_to(REPO_ROOT)), "GROUP_CONCAT (SQLite specific, prefer STRING_AGG for Postgres)"))

print("=== COMPETITIVE VARIANT AUDIT REPORT ===")
print(f"Python 3 Syntax Errors: {len(py_syntax_errors)}")
for path, err in py_syntax_errors[:10]:
    print(f"  - {path}: {err}")

print(f"Python 2 Leftovers: {len(py2_leftovers)}")
for path, err in py2_leftovers[:10]:
    print(f"  - {path}: {err}")

print(f"SQL Dialect Warnings (SQLite vs Postgres): {len(sql_dialect_warnings)}")
for path, err in sql_dialect_warnings[:10]:
    print(f"  - {path}: {err}")
