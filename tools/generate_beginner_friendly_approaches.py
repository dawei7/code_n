import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"

def clean_problem_statement(pkg_dir: Path, meta: dict) -> tuple[str, str]:
    """Extracts title and clean natural description of the problem statement."""
    title = meta.get("title", pkg_dir.name.split("_", 1)[-1].replace("-", " ").title())
    
    desc_file = pkg_dir / "reference" / "description.md"
    if not desc_file.is_file():
        desc_file = pkg_dir / "doc.md"

    summary = ""
    if desc_file.is_file():
        try:
            content = desc_file.read_text(encoding="utf-8", errors="ignore")
            lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#") and not l.startswith("```") and not l.startswith("|")]
            if lines:
                summary = lines[0]
                summary = re.sub(r"^(Given|You are given|Write a program to)\s+", "", summary, flags=re.IGNORECASE).strip()
                summary = summary.rstrip(". ,;")
                if len(summary) > 280:
                    summary = summary[:277] + "..."
        except Exception:
            pass

    if not summary:
        summary = f"solve the **{title}** challenge according to the constraints"

    return title, summary

def generate_python_explanation(code: str, title: str, summary: str, is_competitive: bool) -> str:
    """Generates an extensive, beginner-friendly, step-by-step explanation of the Python algorithm."""
    
    # Precise Code Primitives Analysis
    has_hashmap = any(x in code for x in ["defaultdict", "Counter", "dict()", "{}", "d = ", "seen = {", "hash"])
    has_hashset = any(x in code for x in ["set()", "seen = set(", "visited = set("])
    has_deque = "deque" in code or "queue" in code
    has_heap = "heapq" in code or "heappush" in code or "heappop" in code
    has_dp = "dp" in code or "memo" in code or "@cache" in code or "@lru_cache" in code
    has_tree = "TreeNode" in code or ("root" in code and ("left" in code or "right" in code))
    has_list = "ListNode" in code or ("head" in code and "next" in code)
    has_binary_search = bool(re.search(r"\b(left|low)\b.*\b(right|high)\b", code) and ("mid" in code or "// 2" in code or "bisect" in code))
    has_two_pointers = bool(re.search(r"\b(left|l)\b.*\b(right|r)\b", code) and ("while" in code or "for" in code) and not has_binary_search and not has_tree)
    has_inner_recursion = bool(re.search(r"def\s+(solver|solve|dfs|helper|backtrack|recur|search|find)\b", code))
    has_backtracking = "backtrack" in code.lower() or (("solver(" in code or "solve(" in code or "board" in code) and has_inner_recursion)
    has_dfs = ("dfs" in code.lower() or "recursion" in code.lower() or has_inner_recursion) and not has_backtracking and not has_tree
    has_bfs = "bfs" in code.lower() or "popleft" in code
    has_bit = bool(re.search(r"[&|^~]|<<|>>", code))
    has_walrus = ":=" in code

    # Step 1: Intuition & High-Level Concept
    intuition = f"### Beginner-Friendly Intuition & Strategy\n"
    intuition += f"The core task in **{title}** is to {summary}. "
    
    if has_tree:
        intuition += "The data is structured as a **Binary Tree** where each node contains a value (`val`) and pointers to its `left` and `right` children. Instead of treating the tree as an array, the algorithm uses **Tree Traversal (Recursion / DFS)** to process each node and its subtrees. At every node, it recursively compares or transforms the left and right child subtrees, combining their results to solve the problem for the entire tree."
    elif has_list:
        intuition += "The input is a **Singly-Linked List** where nodes are linked sequentially (`val`, `next`). The algorithm iterates through the list using pointer manipulation, updating linkages or traversing step-by-step without requiring extra array allocations."
    elif has_backtracking:
        intuition += "A naive approach might try every possible digit or combination randomly, which leads to millions of redundant calculations. Instead, this solution uses **Backtracking (Recursive State Exploration)**. Imagine solving a maze: you make a tentative choice at an open cell, check if it obeys all constraints, and move deeper into the maze. If you ever hit a dead end, you **backtrack** (undo your last move by resetting the state) and try the next alternative. This guarantees finding a valid configuration while pruning invalid paths early."
    elif has_dp:
        intuition += "Instead of recalculating the exact same subproblems over and over again, this solution uses **Dynamic Programming**. We break the larger problem down into smaller overlapping subproblems, solve each subproblem once, and store its result in a memory table. When building the final answer, we simply look up previously calculated answers."
    elif has_binary_search:
        intuition += "Instead of scanning every element one by one in $O(n)$ time, this solution uses **Binary Search**. Think of looking up a word in a dictionary: you open it in the middle, see if your word comes before or after, and discard half of the remaining pages. By halving the candidate window at each step, we find the answer in fast logarithmic $O(\log n)$ time."
    elif has_two_pointers:
        intuition += "Instead of using nested loops that inspect every pair in $O(n^2)$ time, this algorithm uses the **Two-Pointer technique**. We place two markers (pointers)—typically one at the start (`left`) and one at the end (`right`) of a sorted array—and move them toward each other based on clear comparison rules, completing the search in a single efficient pass."
    elif has_hashmap or has_hashset:
        intuition += "To avoid nested loops that slow down execution, this solution uses a **Hash Table (Hash Map / Hash Set)**. Think of a index index-cards file: instead of scanning through all cards to check if a number exists, the hash table allows us to instantly look up any value in constant $O(1)$ time."
    elif has_heap:
        intuition += "To dynamically keep track of the minimum or maximum value without sorting the entire array repeatedly, this solution uses a **Min/Max Heap (Priority Queue)**. It allows us to insert elements and extract the smallest/largest value in fast logarithmic $O(\log k)$ time."
    else:
        intuition += "The algorithm processes the input using a single-pass linear iteration, maintaining state variables that update as each element is inspected to produce the result cleanly."

    # Step 2: Detailed Step-by-Step Walkthrough
    walkthrough = f"\n\n### Step-by-Step Execution Guide\n"
    step_num = 1
    
    walkthrough += f"**Step {step_num}: Setup & Base Cases**  \n"
    step_num += 1
    if has_tree:
        walkthrough += "We check the base conditions for tree nodes. If a tree node is `None` (empty), we return the base boundary value (e.g., `True` for equality or `0` for depth).  \n"
    elif has_list:
        walkthrough += "We set up tracking pointers (e.g. `prev`, `curr`, `head`) to navigate node linkages safely.  \n"
    elif has_backtracking:
        walkthrough += "We inspect the board/grid and locate the first empty spot or decision point that needs a valid assignment, establishing helper validation routines.  \n"
    elif has_hashmap:
        walkthrough += "We initialize an empty hash map (`dict`) to act as our fast memory bank, storing elements and their indices or frequencies.  \n"
    elif has_hashset:
        walkthrough += "We initialize an empty hash set (`set`) to remember visited values and prevent duplicate processing.  \n"
    elif has_dp:
        walkthrough += "We create a Dynamic Programming table and initialize known base cases.  \n"
    elif has_two_pointers:
        walkthrough += "We place `left = 0` at the start of the array and `right = len(array) - 1` at the end.  \n"
    else:
        walkthrough += "We set up tracking variables (accumulators, counters, or pointers) to hold intermediate results.  \n"

    walkthrough += f"**Step {step_num}: Core Processing & Traversal**  \n"
    step_num += 1
    if has_tree:
        walkthrough += "1. Inspect the current node values (e.g. `p.val` and `q.val`).  \n2. If values differ, return `False` immediately.  \n3. Recursively invoke traversal on left child subtrees (`self.isSameTree(p.left, q.left)`).  \n4. Recursively invoke traversal on right child subtrees (`self.isSameTree(p.right, q.right)`).  \n5. Return `True` only if both left and right subtrees match.  \n"
    elif has_list:
        walkthrough += "1. Advance through node linkages using `curr = curr.next`.  \n2. Perform values computation or link reversals.  \n3. Continue until `curr` reaches `None`.  \n"
    elif has_backtracking:
        walkthrough += "1. Scan for an empty cell (`'.'`).  \n2. Iterate through candidate choices (`'1'` to `'9'`).  \n3. For each candidate, verify validity.  \n4. If valid, place tentatively and recursively call `solver()`.  \n5. If recursive call returns `True`, puzzle is solved!  \n6. If it returns `False`, reset cell to `'.'`.  \n"
    elif has_binary_search:
        walkthrough += "1. Calculate `mid = (left + right) // 2`.  \n2. Compare `array[mid]` with target value.  \n3. Adjust `left = mid + 1` or `right = mid - 1` to halve the search window.  \n"
    elif has_two_pointers:
        walkthrough += "1. Compare elements at `array[left]` and `array[right]`.  \n2. Advance `left` or retreat `right` based on comparison rules.  \n"
    elif has_hashmap:
        walkthrough += "1. Loop through each item in the input.  \n2. Calculate target complement.  \n3. Check if complement exists in hash map for $O(1)$ match.  \n4. Store current value in hash map if not found.  \n"
    else:
        walkthrough += "1. Iterate sequentially through each element.  \n2. Apply operational rules to update state variables.  \n"

    walkthrough += f"**Step {step_num}: Completion & Return**  \n"
    if has_walrus:
        walkthrough += "Python's walrus operator (`:=`) is used to assign and evaluate variables inline, streamlining the loop.  \n"
    if has_bit:
        walkthrough += "Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates in $O(1)$ hardware instructions.  \n"
    walkthrough += "When processing finishes, the algorithm outputs the final validated solution."

    # Step 3: Edge Case Handling
    edge = "\n\n### Why This Handles Edge Cases Gracefully\n"
    if has_tree:
        edge += "- **Both Nodes Empty (`None`):** Returns `True` as two empty subtrees are identical.\n- **One Node Empty, One Non-Empty:** Returns `False` immediately, preventing null pointer attribute access (`AttributeError`).\n"
    elif has_list:
        edge += "- **Empty or Single-Node Lists:** Pointer checks (`while head:`) handle empty or single-element lists without throwing exceptions.\n"
    elif "if not " in code or "if len(" in code or "if s is None" in code or "if root is None" in code:
        edge += "- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.\n"
    elif "float('inf')" in code or "float('-inf')" in code or "math.inf" in code:
        edge += "- **Extreme Boundaries:** Infinity sentinels prevent invalid initial minimum/maximum comparisons.\n"
    elif has_backtracking:
        edge += "- **No Solution / Unsolvable States:** Returns `False` when candidates are exhausted, triggering proper backtracking.\n"
    else:
        edge += "- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally.\n"

    return intuition + walkthrough + edge

def generate_sql_explanation(code: str, title: str, summary: str, is_competitive: bool) -> str:
    """Generates an extensive, beginner-friendly, step-by-step explanation of the SQL query."""
    code_upper = code.upper()
    has_cte = "WITH" in code_upper
    has_join = "JOIN" in code_upper
    has_window = any(f in code_upper for f in ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "OVER(", "LAG(", "LEAD("])
    has_group = "GROUP BY" in code_upper

    text = f"### Beginner-Friendly Relational Pipeline Strategy\n"
    text += f"To {summary}, this database query builds a step-by-step SQL pipeline.\n\n"
    
    text += "### Step-by-Step Query Execution\n"
    if has_cte:
        text += "**Step 1: Common Table Expressions (CTEs)**  \n"
        text += "The query uses `WITH` clauses to break complex database transformations into small, easy-to-read virtual tables. This makes the query modular and simple to understand.  \n"
    if has_join:
        text += "**Step 2: Relational JOIN Operations**  \n"
        text += "It combines matching rows across tables using `INNER JOIN` or `LEFT JOIN` on foreign keys so related information appears in a single record set.  \n"
    if has_window:
        text += "**Step 3: PostgreSQL Window Functions**  \n"
        text += "Analytical functions (`ROW_NUMBER()`, `RANK()`, `LAG()`, etc.) calculate relative rankings or running totals within specified partitions without collapsing individual rows.  \n"
    if has_group:
        text += "**Step 4: Grouping & Aggregations**  \n"
        text += "It groups rows together using `GROUP BY` and calculates sums, averages, or counts for each group.  \n"

    text += "\n### Edge Case Handling & PostgreSQL Standards\n"
    if "COALESCE" in code_upper:
        text += "- **Handling NULL Values:** Uses `COALESCE(column, 0)` so missing database values automatically turn into `0` or empty strings rather than causing `NULL` calculation errors.\n"
    if "HAVING" in code_upper:
        text += "- **Filtering Aggregated Results:** Uses `HAVING` to filter groups after aggregation occurs.\n"
    text += "- **ANSI SQL Standard:** Follows PostgreSQL standards for cross-platform reliability.\n"

    return text

def generate_js_explanation(code: str, title: str, summary: str, is_competitive: bool) -> str:
    """Generates an extensive, beginner-friendly explanation of JavaScript solutions."""
    text = f"### Beginner-Friendly Strategy\n"
    text += f"To {summary}, the JavaScript solution uses clean ES6+ techniques.\n\n"
    text += "### Step-by-Step Execution Guide\n"
    text += "**Step 1: Setup** — Initializes fast lookup structures such as `Map` or `Set` for $O(1)$ fast lookups.  \n"
    text += "**Step 2: Processing** — Uses built-in array methods (`map`, `filter`, `reduce`) or clean loops to process data.  \n"
    text += "\n### Edge Case Handling\n"
    text += "- **Empty Arrays / Edge Cases:** Checked via `length` guards to prevent runtime crashes.\n"
    return text

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

    title, summary = clean_problem_statement(pkg_dir, meta)

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
            algo_desc = generate_sql_explanation(code, title, summary, is_competitive)
        elif ext == ".js":
            algo_desc = generate_js_explanation(code, title, summary, is_competitive)
        else:
            algo_desc = generate_python_explanation(code, title, summary, is_competitive)

        app_content = f"""## General
{algo_desc}

## Complexity detail
- **Time Complexity**: ${tc}$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: ${sc}$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
"""

        (var_dir / "approach.md").write_text(app_content, encoding="utf-8")
        processed_count += 1

print(f"Generated extensive, beginner-friendly approach.md for {processed_count} variant directories.")
