"""Migrate all LeetCode SQL problem solutions and templates to PostgreSQL."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
leetcode_dir = ROOT / "dsa" / "leetcode"


def convert_sql_to_postgres(code: str) -> str:
    # 1. Comment headers
    code = re.sub(
        r"#\s*Write your MySQL query statement below",
        "-- Write your PostgreSQL query statement below",
        code,
        flags=re.IGNORECASE,
    )
    code = re.sub(r"^#\s*(.*)$", r"-- \1", code, flags=re.MULTILINE)

    # 2. String literal column aliases: AS 'Something' -> AS "Something" or AS Something
    code = re.sub(r"\bAS\s+'([A-Za-z0-9_]+)'", r'AS "\1"', code, flags=re.IGNORECASE)

    # 3. IFNULL -> COALESCE
    code = re.sub(r"\bIFNULL\s*\(", "COALESCE(", code, flags=re.IGNORECASE)

    # 4. LIMIT offset, count -> LIMIT count OFFSET offset
    code = re.sub(
        r"\bLIMIT\s+(\d+)\s*,\s*(\d+)",
        r"LIMIT \2 OFFSET \1",
        code,
        flags=re.IGNORECASE,
    )

    # 5. GROUP_CONCAT -> STRING_AGG
    def _fix_group_concat(match: re.Match) -> str:
        inner = match.group(1).strip()
        # Check for SEPARATOR
        sep_match = re.search(r"SEPARATOR\s+('[^']*'|\"[^\"]*\")", inner, re.IGNORECASE)
        sep = sep_match.group(1) if sep_match else "',' " if "SEPARATOR" not in inner else "','"
        if sep_match:
            inner_no_sep = inner[:sep_match.start()].strip() + inner[sep_match.end():].strip()
        else:
            inner_no_sep = inner

        # Check for ORDER BY
        order_match = re.search(r"ORDER\s+BY\s+(.*)", inner_no_sep, re.IGNORECASE)
        if order_match:
            order_clause = f" ORDER BY {order_match.group(1).strip()}"
            expr = inner_no_sep[:order_match.start()].strip()
        else:
            order_clause = ""
            expr = inner_no_sep.strip()

        # Handle default comma separator
        if not sep_match:
            sep = "','"

        return f"STRING_AGG({expr}, {sep}{order_clause})"

    code = re.sub(r"\bGROUP_CONCAT\s*\((.*?)\)", _fix_group_concat, code, flags=re.IGNORECASE | re.DOTALL)

    return code


def update_all_sql_packages() -> None:
    updated_solutions = 0
    updated_manifests = 0
    updated_templates = 0

    for pkg in sorted(leetcode_dir.iterdir()):
        if not pkg.is_dir() or pkg.name.startswith(("_", ".")):
            continue

        meta_file = pkg / "metadata.json"
        if not meta_file.is_file():
            continue
        meta = json.loads(meta_file.read_text(encoding="utf-8"))
        is_sql = meta.get("primary_language") == "sql" or meta.get("category") == "database"

        # Check solution files
        sol_files = list(pkg.glob("variants/optimal/**/solution.sql")) + list(pkg.glob("variants/optimal/solution.sql"))
        if sol_files:
            is_sql = True

        if not is_sql:
            continue

        # 1. Update solution.sql
        for sf in sol_files:
            original = sf.read_text(encoding="utf-8")
            converted = convert_sql_to_postgres(original)
            if converted != original:
                sf.write_text(converted, encoding="utf-8")
                updated_solutions += 1

        # 2. Update template.sql
        tmpl_file = pkg / "template.sql"
        if tmpl_file.is_file():
            t_orig = tmpl_file.read_text(encoding="utf-8")
            t_conv = convert_sql_to_postgres(t_orig)
            if t_conv != t_orig:
                tmpl_file.write_text(t_conv, encoding="utf-8")
                updated_templates += 1

        # 3. Update submission.json
        manifest_file = pkg / "variants" / "optimal" / "submission.json"
        if manifest_file.is_file():
            try:
                mdata = json.loads(manifest_file.read_text(encoding="utf-8"))
                if mdata.get("language") == "mysql":
                    mdata["language"] = "postgresql"
                    manifest_file.write_text(json.dumps(mdata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                    updated_manifests += 1
            except Exception:
                pass

    print(f"Postgres migration summary:")
    print(f"  - Updated {updated_solutions} solution.sql files")
    print(f"  - Updated {updated_templates} template.sql files")
    print(f"  - Updated {updated_manifests} submission.json manifests")


if __name__ == "__main__":
    update_all_sql_packages()
