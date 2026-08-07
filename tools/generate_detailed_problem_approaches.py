import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"

def extract_problem_goal(pkg_dir: Path, meta: dict) -> str:
    """Extracts a clean summary of the problem goal from reference/description.md, doc.md, or metadata.json."""
    title = meta.get("title", pkg_dir.name.split("_", 1)[-1].replace("-", " ").title())
    
    desc_file = pkg_dir / "reference" / "description.md"
    if not desc_file.is_file():
        desc_file = pkg_dir / "doc.md"

    if desc_file.is_file():
        try:
            content = desc_file.read_text(encoding="utf-8", errors="ignore")
            lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#") and not l.startswith("```") and not l.startswith("|")]
            if lines:
                para = lines[0]
                cleaned = re.sub(r"^(Given|You are given)\s+", "", para, flags=re.IGNORECASE).strip()
                cleaned = cleaned.rstrip(". ,;")
                if len(cleaned) > 220:
                    cleaned = cleaned[:217] + "..."
                return f"Given {cleaned}"
        except Exception:
            pass

    return f"To solve **{title}**"

def elaborate_python_algorithm(code: str, title: str, goal: str, is_competitive: bool) -> str:
    """Builds a rich, problem-specific narrative connecting the problem goal to the solution algorithm."""
    data_structures = []
    control_flow = []
    key_operations = []
    edge_cases = []

    if "defaultdict" in code or "Counter" in code or "dict()" in code or "{}" in code or "d = " in code or "seen = {" in code:
        data_structures.append("a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access")
    if "set()" in code or "seen = set(" in code or "visited = set(" in code:
        data_structures.append("a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time")
    if "deque" in code or "queue" in code:
        data_structures.append("a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends")
    if "heapq" in code or "heappush" in code or "heappop" in code:
        data_structures.append("a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering")
    if "dp" in code or "memo" in code:
        data_structures.append("a dynamic programming memoization table to cache intermediate subproblem states")
    if "TreeNode" in code:
        data_structures.append("binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies")
    if "ListNode" in code:
        data_structures.append("linked list node pointers (`val`, `next`) to process sequential node chains")

    if re.search(r"\b(left|low)\b.*\b(right|high)\b", code) and ("mid" in code or "// 2" in code or "bisect" in code):
        control_flow.append("binary search over the search space to achieve logarithmic reduction")
    elif re.search(r"\b(left|l)\b.*\b(right|r)\b", code) and ("while" in code or "for" in code):
        control_flow.append("a two-pointer approach to shrink boundaries or maintain a sliding window")
    elif "dfs" in code.lower() or "backtrack" in code.lower():
        control_flow.append("depth-first search (DFS) recursion to explore valid decision branches")
    elif "bfs" in code.lower() or "popleft" in code:
        control_flow.append("breadth-first search (BFS) level-order traversal using a queue")
    elif "enumerate" in code or "for " in code:
        control_flow.append("a single-pass linear scan through input elements")

    if re.search(r"[&|^~]|<<|>>", code):
        key_operations.append("bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates")
    if ":=" in code:
        key_operations.append("the walrus operator (`:=`) for inline assignment and evaluation")

    if "if not " in code or "if len(" in code or "if s is None" in code or "if root is None" in code:
        edge_cases.append("guards against empty/null inputs via early returns")
    if "float('inf')" in code or "float('-inf')" in code or "math.inf" in code:
        edge_cases.append("uses infinity sentinels for safe boundary initialization")
    if "modulo" in code or "10**9 + 7" in code or "10**9+7" in code or "%" in code:
        edge_cases.append("applies modulo arithmetic to prevent integer overflow")

    narrative = f"{goal}, the algorithm "
    if control_flow:
        narrative += "executes " + ", ".join(control_flow) + ". "
    else:
        narrative += f"solves **{title}** directly. "

    if data_structures:
        narrative += "It utilizes " + ", ".join(data_structures) + ". "

    if key_operations:
        narrative += "Key operations include " + ", ".join(key_operations) + ". "

    if edge_cases:
        narrative += "Edge case handling: " + ", ".join(edge_cases) + "."

    return narrative.strip()

def elaborate_sql_algorithm(code: str, title: str, goal: str, is_competitive: bool) -> str:
    code_upper = code.upper()
    parts = []
    if "WITH" in code_upper:
        parts.append("Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries")
    if "JOIN" in code_upper:
        parts.append("relational `JOIN` operations to correlate matching records across tables")
    if any(f in code_upper for f in ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "OVER(", "LAG(", "LEAD("]):
        parts.append("window functions for positional ranking and partition analytical operations")
    if "GROUP BY" in code_upper:
        parts.append("`GROUP BY` aggregations to summarize record groups")

    edge_cases = []
    if "COALESCE" in code_upper:
        edge_cases.append("replaces `NULL` values using `COALESCE` guards")
    if "HAVING" in code_upper:
        edge_cases.append("filters aggregated group results via `HAVING` predicates")

    narrative = f"{goal}, the database query "
    if parts:
        narrative += "executes a relational pipeline using " + ", ".join(parts) + "."
    else:
        narrative += f"executes a relational database query for **{title}**."

    if edge_cases:
        narrative += " Edge case handling: " + ", ".join(edge_cases) + "."

    return narrative.strip()

def elaborate_js_algorithm(code: str, title: str, goal: str, is_competitive: bool) -> str:
    parts = []
    if "Map(" in code or "Set(" in code:
        parts.append("ES6 `Map`/`Set` collections for $O(1)$ fast key lookups")
    if "reduce(" in code or "map(" in code or "filter(" in code:
        parts.append("functional array iteration methods")

    narrative = f"{goal}, the JavaScript algorithm "
    if parts:
        narrative += "uses " + ", ".join(parts) + "."
    else:
        narrative += f"implements the solution for **{title}**."

    if "if (" in code or "length" in code:
        narrative += " Edge case handling: guards against empty inputs using array/string length checks."

    return narrative.strip()

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
    goal = extract_problem_goal(pkg_dir, meta)

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
            algo_desc = elaborate_sql_algorithm(code, title, goal, is_competitive)
        elif ext == ".js":
            algo_desc = elaborate_js_algorithm(code, title, goal, is_competitive)
        else:
            algo_desc = elaborate_python_algorithm(code, title, goal, is_competitive)

        app_content = f"""## General
{algo_desc}

## Complexity detail
- **Time Complexity**: ${tc}$ — Operation count bound.
- **Space Complexity**: ${sc}$ — Auxiliary memory allocation bound.
"""

        (var_dir / "approach.md").write_text(app_content, encoding="utf-8")
        processed_count += 1

print(f"Generated detailed problem-elaborated approach.md for {processed_count} variant directories.")
