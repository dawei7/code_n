import re
import json
from pathlib import Path

repo_root = Path('.')
leetcode_dir = repo_root / 'dsa' / 'leetcode'

sql_pkgs = []
for pkg in sorted(leetcode_dir.iterdir()):
    if not pkg.is_dir() or pkg.name.startswith(('_', '.')):
        continue
    meta_file = pkg / 'metadata.json'
    if not meta_file.exists():
        continue
    meta = json.loads(meta_file.read_text(encoding='utf-8'))
    if meta.get('primary_language') == 'sql' or meta.get('category') == 'database':
        sql_pkgs.append(pkg)

print(f"Total SQL packages: {len(sql_pkgs)}")

def fix_sql_for_postgres(code: str) -> str:
    original = code
    
    # 1. Fix MySQL comments
    code = re.sub(r'# Write your MySQL query statement below', '-- Write your PostgreSQL query statement below', code)
    code = re.sub(r'^#\s*(.*)$', r'-- \1', code, flags=re.MULTILINE)
    
    # 2. Fix single quoted aliases: AS 'Something' -> AS "Something"
    code = re.sub(r'\bAS\s+\'([^\']+)\'', r'AS "\1"', code, flags=re.IGNORECASE)
    
    # 3. Fix LIMIT offset, count -> LIMIT count OFFSET offset
    code = re.sub(r'\bLIMIT\s+(\d+)\s*,\s*(\d+)', r'LIMIT \2 OFFSET \1', code, flags=re.IGNORECASE)
    
    # 4. Fix IFNULL -> COALESCE
    code = re.sub(r'\bIFNULL\s*\(', 'COALESCE(', code, flags=re.IGNORECASE)
    
    # 5. Fix GROUP_CONCAT(col SEPARATOR sep) -> STRING_AGG(col, sep)
    def fix_group_concat(match):
        inner = match.group(1)
        # check if SEPARATOR is used
        sep_match = re.search(r'SEPARATOR\s+([^\)]+)', inner, re.IGNORECASE)
        if sep_match:
            sep = sep_match.group(1).strip()
            col = inner[:sep_match.start()].strip()
            return f'STRING_AGG({col}, {sep})'
        return f"STRING_AGG({inner}, ',')"
    code = re.sub(r'\bGROUP_CONCAT\s*\(([^\)]+)\)', fix_group_concat, code, flags=re.IGNORECASE)
    
    return code

modified_count = 0
for pkg in sql_pkgs:
    sol_files = list(pkg.glob('variants/optimal/**/solution.sql')) + list(pkg.glob('variants/optimal/solution.sql'))
    for sf in sol_files:
        code = sf.read_text(encoding='utf-8')
        fixed = fix_sql_for_postgres(code)
        if fixed != code:
            sf.write_text(fixed, encoding='utf-8')
            modified_count += 1

print(f"Applied standard PostgreSQL syntax transforms to {modified_count} solutions.")
