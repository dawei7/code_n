"""Rate every cOde(n) challenge with:
  - my_difficulty (1-10): how hard the algorithm is to implement
    correctly on a whiteboard.
  - my_relevance  (1-10): how often the algorithm comes up in
    coding interviews (1 = never, 10 = must-know).

Outputs a markdown table grouped by category, plus a summary
showing agreement/disagreement with the existing `difficulty`
field on the spec.

Scoring heuristic (a starting point; hand-tunable per outlier):
  - Base by category (see _CATEGORY_BASE).
  - Adjust by name keyword (advanced / research / obscure).
  - Adjust by required complexity (O(2^n) usually harder).
  - Relevance: prioritzes what real interviewers ask. BFS/DFS,
    binary search, hash tables, basic DP, basic sort all rank
    high; segment trees, suffix arrays, max-flow rank low unless
    they're a canonical interview topic.
"""
from __future__ import annotations

from challenges.registry import CHALLENGE_REGISTRY


# --- Per-category baseline (difficulty, relevance) --------------
# A reasonable starting point for "the average problem in this
# category". Outliers (e.g., "Hello Grid" in `intro` is d=1; "TSP
# Held-Karp" in `graphs` is d=7) get adjusted by the keyword
# rules below.
_CATEGORY_BASE: dict[str, tuple[int, int]] = {
    "approximation":    (5, 2),   # rarely tested; theory-heavy
    "backtracking":     (5, 6),   # classic interview (permutations, sudoku)
    "branch_and_bound": (6, 3),   # specialized
    "bit_manipulation": (3, 7),   # very common in screens
    "divide_conquer":   (5, 6),   # common pattern, careful indices
    "dynamic":          (5, 9),   # THE interview topic
    "fenwick":          (4, 4),   # niche data structure
    "flow":             (6, 2),   # advanced; rare in interviews
    "geometric":        (5, 2),   # rare; computational geometry
    "graphs":           (5, 8),   # BFS/DFS/Dijkstra/Union-Find - core
    "greedy":           (4, 7),   # common, well-known patterns
    "hashing":          (4, 9),   # hash maps - every interview
    "heap":             (5, 6),   # top-K is common; rest is rarer
    "intro":            (1, 1),   # sanity check
    "linked_list":      (3, 7),   # classic list manipulation
    "math":             (4, 5),   # modular arithmetic etc; some common
    "queue":            (3, 4),   # BFS-related; moderate
    "randomized":       (5, 3),   # niche
    "recursion":        (3, 7),   # recursion drills; very common
    "searching":        (3, 8),   # binary search - MUST know
    "segment_tree":     (5, 3),   # advanced DS; rare in interviews
    "sorting":          (4, 8),   # sort algorithms - core
    "stack":            (4, 7),   # parentheses/eval; very common
    "strings":          (4, 7),   # anagram / palindrome etc - common
    "suffix_array":     (5, 2),   # advanced; very rare in interviews
    "trees":            (4, 8),   # tree traversals + BFS on tree - core
    "trie":             (3, 5),   # asked sometimes
}


# --- Per-name keyword adjustments -------------------------------
# Format: (substring in name (case-insensitive), d_delta, r_delta)
_NAME_ADJUST: list[tuple[str, int, int]] = [
    # Trivial intros
    ("hello",            -3,  0),
    ("power of two",     -2,  0),

    # High-difficulty / research algorithms
    ("christofides",     +2, -1),
    ("fptas",            +2, -1),
    ("strassen",         +2, -1),
    ("push-relabel",     +1, -1),
    ("held-karp",        +1,  0),
    ("optimal binary search tree", +1,  0),
    ("boolea",           +1,  0),  # Boolean parenthesization
    ("egg dropp",        0, -1),  # specialized DP, asked rarely
    ("matrix chain",     +1,  0),
    ("freivald",         +1, -2),
    ("karger",           +1, -1),
    ("karatsuba",        +1,  0),
    ("kasai",            0,  -1),
    ("z-algorithm",      0,  0),
    ("rabin-karp",       0,  0),
    ("kmp",              0,  0),
    ("avl",              +1,  0),
    ("trie",             0,  0),
    ("patience sort",    0,  0),

    # Common interview topics
    ("two sum",          0,  0),
    ("longest substring", 0, 0),
    ("group anagrams",   0,  0),
    ("coin change",      0,  0),
    ("knapsack",         0,  0),
    ("lcs",              0,  0),
    ("edit distance",    0,  0),
    ("word break",       0,  0),
    ("longest increasing", 0, 0),
    ("trapping rain",    0,  0),
    ("largest rectangle", 0, 0),
    ("next greater",     0,  0),
    ("balanced parentheses", 0, 0),
    ("reverse linked",   0,  0),
    ("cycle",            0,  0),
    ("bfs",              0,  0),
    ("dfs",              0,  0),
    ("dijkstra",         0,  0),
    ("union-find",       0,  0),
    ("binary search",    0,  0),
    ("quickselect",      0,  0),
    ("mergesort",        0,  0),
    ("mergesort",        0,  0),
    ("merge sort",       0,  0),
    ("quick sort",       0,  0),
    ("heap sort",        0,  0),
    ("top k",            0,  0),
    ("median",           0,  0),
    ("sliding window",   0,  0),
    ("reverse bits",     0,  0),
    ("xor",              0,  0),
    ("two pointers",     0,  0),
    ("fast/slow",        0,  0),
    ("prefix sum",       0,  0),
    ("fibonacci",        0,  0),

    # Reduce relevance: obscure / never asked
    ("monte carlo",      0,  -2),
    ("est. pi",          0,  -2),  # estimating pi
    ("approximation",    0,  -1),
    ("approx",           0,  -1),
    ("fractional knapsack", 0, -1),
    ("bin packing",      0,  -1),
    ("first-fit",        0,  -1),
    ("huffman",          0,  -1),
    ("gale-shapley",     0,  -1),
    ("stable marriage",  0,  -1),
    ("christofides",     0,  -1),
    ("hungarian",        0,  -1),
    ("reduced matrix",   0,  -1),
    ("k-th smallest",    0,  0),
    ("order-statistic",  0,  -1),
    ("union-find",       0,  0),

    # Bump difficulty: mathematically heavy
    ("sieve",            0,  0),
    ("miller-rabin",     +1, -1),
    ("carmichael",       +1, -1),
    ("euler totient",    0,  -1),
    ("modular inverse",  0,  0),
    ("modular exp",      0,  0),
    ("extended euclid",  0,  0),
]


# --- Per-complexity adjustments --------------------------------
_COMPLEX_DELTA: dict[str, tuple[int, int]] = {
    "O(2^n)":    (+1,  0),
    "O(n^3)":    (+1,  0),
    "O(n log n)": (0,   0),
    "O(n^2)":    (0,   0),
    "O(n)":      (0,   0),
    "O(log n)":  (0,   0),
    "O(1)":      (-1,  0),
}


def rate(name: str, category: str, complexity_value: str) -> tuple[int, int]:
    """Return (my_difficulty, my_relevance)."""
    base_d, base_r = _CATEGORY_BASE.get(category, (5, 5))
    d, r = base_d, base_r

    name_lc = name.lower()
    for needle, d_delta, r_delta in _NAME_ADJUST:
        if needle in name_lc:
            d += d_delta
            r += r_delta

    c_delta = _COMPLEX_DELTA.get(complexity_value, (0, 0))
    d += c_delta[0]
    r += c_delta[1]

    # Clamp to 1..10
    d = max(1, min(10, d))
    r = max(1, min(10, r))
    return d, r


# --- Render ----------------------------------------------------

def main() -> None:
    rows: list[dict] = []
    for cid, cls in sorted(CHALLENGE_REGISTRY.items()):
        spec = cls()._spec
        my_d, my_r = rate(spec.name, spec.category, spec.required_complexity.value)
        rows.append({
            "id": cid,
            "name": spec.name,
            "category": spec.category,
            "complexity": spec.required_complexity.value,
            "existing_d": spec.difficulty,
            "my_d": my_d,
            "my_r": my_r,
        })

    # Group by category, then by id
    by_cat: dict[str, list[dict]] = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r)

    # --- Markdown table per category --------------------------------
    print("# cOde(n) Algorithms — Difficulty & Relevance\n")
    print("| Category | ID | Name | Complexity | Existing d | My d | My r |")
    print("|---|---|---|---|---:|---:|---:|")
    for cat in sorted(by_cat):
        print(f"| **{cat}** | | | | | | |")
        for r in by_cat[cat]:
            print(
                f"|  | `{r['id']}` | {r['name']} | "
                f"{r['complexity']} | {r['existing_d']} | "
                f"**{r['my_d']}** | **{r['my_r']}** |"
            )

    # --- Per-category summary --------------------------------------
    print("\n## Per-category summary\n")
    print("| Category | # | avg d (existing) | avg d (mine) | avg r (mine) |")
    print("|---|---:|---:|---:|---:|")
    for cat in sorted(by_cat):
        rs = by_cat[cat]
        n = len(rs)
        avg_existing = sum(r["existing_d"] for r in rs) / n
        avg_mine_d = sum(r["my_d"] for r in rs) / n
        avg_mine_r = sum(r["my_r"] for r in rs) / n
        print(
            f"| {cat} | {n} | {avg_existing:.1f} | {avg_mine_d:.1f} | {avg_mine_r:.1f} |"
        )

    # --- Where existing_d vs my_d disagree by >= 2 ---------------
    print("\n## Where my difficulty disagrees with existing by >= 2\n")
    print("| ID | Category | Name | Existing | Mine | Reason |")
    print("|---|---|---|---:|---:|---|")
    for r in rows:
        if abs(r["existing_d"] - r["my_d"]) >= 2:
            print(
                f"| `{r['id']}` | {r['category']} | {r['name']} | "
                f"{r['existing_d']} | {r['my_d']} |  |"
            )


if __name__ == "__main__":
    main()
