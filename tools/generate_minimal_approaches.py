import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"

def analyze_python_code(code: str, title: str, is_competitive: bool) -> str:
    """Generates a concise algorithm description based on Python code analysis."""
    data_structures = []
    control_flow = []
    key_operations = []

    if "defaultdict" in code or "Counter" in code or "dict()" in code or "{}" in code or "d = " in code or "seen = {" in code:
        data_structures.append("hash map (`dict`) for $O(1)$ average lookup")
    if "set()" in code or "seen = set(" in code or "visited = set(" in code:
        data_structures.append("hash set (`set`) for $O(1)$ existence checks")
    if "deque" in code or "queue" in code:
        data_structures.append("double-ended queue (`deque`) for $O(1)$ operations")
    if "heapq" in code or "heappush" in code or "heappop" in code:
        data_structures.append("priority queue (`heapq`) for dynamic minimum/maximum tracking")
    if "dp" in code or "memo" in code:
        data_structures.append("dynamic programming memoization store")
    if "TreeNode" in code:
        data_structures.append("tree traversal nodes (`val`, `left`, `right`)")
    if "ListNode" in code:
        data_structures.append("linked list nodes (`val`, `next`)")

    if re.search(r"\b(left|low)\b.*\b(right|high)\b", code) and ("mid" in code or "// 2" in code or "bisect" in code):
        control_flow.append("binary search over search space")
    elif re.search(r"\b(left|l)\b.*\b(right|r)\b", code) and ("while" in code or "for" in code):
        control_flow.append("two-pointer iteration")
    elif "dfs" in code.lower() or "backtrack" in code.lower():
        control_flow.append("depth-first search / backtracking recursion")
    elif "bfs" in code.lower() or "popleft" in code:
        control_flow.append("breadth-first search queue traversal")
    elif "enumerate" in code or "for " in code:
        control_flow.append("single-pass sequential iteration")

    if re.search(r"[&|^~]|<<|>>", code):
        key_operations.append("bitwise operations (`&`, `|`, `^`, `<<`, `>>`)")
    if ":=" in code:
        key_operations.append("walrus operator (`:=`) inline assignment")

    parts = []
    if control_flow:
        parts.append("Uses " + ", ".join(control_flow) + ".")
    if data_structures:
        parts.append("Maintains " + ", ".join(data_structures) + ".")
    if key_operations:
        parts.append("Applies " + ", ".join(key_operations) + ".")

    if not parts:
        variant_type = "competitive micro-optimized" if is_competitive else "optimal"
        return f"Implements the {variant_type} algorithm for **{title}**."

    return " ".join(parts)

def analyze_sql_code(code: str, title: str, is_competitive: bool) -> str:
    code_upper = code.upper()
    parts = []
    if "WITH" in code_upper:
        parts.append("Common Table Expressions (CTEs)")
    if "JOIN" in code_upper:
        parts.append("relational JOINs")
    if any(f in code_upper for f in ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "OVER(", "LAG(", "LEAD("]):
        parts.append("window functions")
    if "GROUP BY" in code_upper:
        parts.append("GROUP BY aggregations (`COALESCE`, `STRING_AGG`)")

    if parts:
        return f"Executes a SQL query for **{title}** using " + ", ".join(parts) + "."
    return f"Executes a relational database query for **{title}**."

def analyze_js_code(code: str, title: str, is_competitive: bool) -> str:
    parts = []
    if "Map(" in code or "Set(" in code:
        parts.append("ES6 Map/Set lookup structures")
    if "reduce(" in code or "map(" in code or "filter(" in code:
        parts.append("JavaScript array iteration methods")

    if parts:
        return f"Executes JavaScript logic for **{title}** using " + ", ".join(parts) + "."
    return f"Implements the JavaScript solution for **{title}**."

processed_count = 0

for pkg_dir in LEETCODE_ROOT.iterdir():
    if not pkg_dir.is_dir() or pkg_dir.name.startswith("_"):
        continue

    meta_file = pkg_dir / "metadata.json"
    meta = {}
    if meta_file.is_file():
        try:
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    title = meta.get("title", pkg_dir.name.split("_", 1)[-1].replace("-", " ").title())

    manifest_file = pkg_dir / "solution_variants.json"
    manifest = {}
    if manifest_file.is_file():
        try:
            manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    variants_map = {}
    if "variants" in manifest:
        for v in manifest["variants"]:
            variants_map[v.get("id")] = v

    variants_dir = pkg_dir / "variants"
    if not variants_dir.is_dir():
        continue

    for var_dir in variants_dir.iterdir():
        if not var_dir.is_dir():
            continue

        var_id = var_dir.name
        is_competitive = (var_id == "competitive")
        v_info = variants_map.get(var_id, {})
        tc = v_info.get("time_complexity", "O(N)")
        sc = v_info.get("space_complexity", "O(1)")

        sols = list(var_dir.glob("solution.*")) + list(var_dir.glob("solutions/solution.*"))
        code = ""
        ext = ".py"
        if sols:
            sol_file = sols[0]
            ext = sol_file.suffix.lower()
            code = sol_file.read_text(encoding="utf-8", errors="ignore")

        if ext == ".sql":
            algo_desc = analyze_sql_code(code, title, is_competitive)
        elif ext == ".js":
            algo_desc = analyze_js_code(code, title, is_competitive)
        else:
            algo_desc = analyze_python_code(code, title, is_competitive)

        app_content = f"""## General
{algo_desc}

## Complexity detail
- **Time Complexity**: ${tc}$ — Operation count bound.
- **Space Complexity**: ${sc}$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Algorithm design:** Describes the specific algorithmic approach used in the solution.
- **Complexity bounds:** Declares the precise time and space complexity guarantees.
"""

        (var_dir / "approach.md").write_text(app_content, encoding="utf-8")
        processed_count += 1

print(f"Generated minimal solution-dependent approach.md for {processed_count} variant directories.")
