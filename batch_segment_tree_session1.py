"""Spec generator input - 3 more segment-tree specs for Session 1.

Covers the GfG segment-tree topic list that segtree_01..03
(Build, Range Sum Query, Point Update) don't already cover:

  segtree_04  Range Minimum Query (RMQ)         (min-segment tree, O(log n))
  segtree_05  Range Update + Lazy Propagation   (range add, range sum, O(log n))
  segtree_06  Range Min + Range Update (Lazy)   (min + lazy, O(log n))

After this batch, segment_tree.py covers the canonical
segment-tree extensions from GfG.

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module segment_tree \\
        --input batch_segment_tree_session1.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # segtree_04: Range Minimum Query (RMQ)
    # ============================================================
    {
        "id": "segtree_04",
        "name": "Range Minimum Query",
        "category": "segment_tree",
        "difficulty": 4,
        "complexity": "O_LOG_N",
        "description": (
            "Build a min-segment tree on arr (each node stores\n"
            "the minimum of its sub-range). For each query\n"
            "(l, r), descend into the tree collecting the\n"
            "minimums that exactly tile [l, r]. Return the\n"
            "list of q range minimums. O(log n) per query.\n"
            "Source: https://www.geeksforgeeks.org/dsa/segment-tree-range-minimum-query/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/segment-tree-range-minimum-query/",
        "params": ["arr", "n", "queries", "q"],
        "inputs": {
            "arr": "list of n integers.",
            "n": "length of arr.",
            "queries": "list of (l, r) tuples.",
            "q": "number of queries.",
        },
        "returns": "a list of q range minimums.",
        "solve": '''
def solve(arr, n, queries, q):
    """Range Minimum Query via segment tree."""
    if n == 0:
        return [0] * q
    tree = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
        else:
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return float("inf")
        if l <= lo and hi <= r:
            return tree[node]
        mid = (lo + hi) // 2
        return min(query(2 * node, lo, mid, l, r),
                   query(2 * node + 1, mid + 1, hi, l, r))

    build(1, 0, n - 1)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 12))
arr = [rng.randint(0, 99) for _ in range(n)]
n_q = max(1, min(n, 4))
queries = []
for _ in range(n_q):
    l = rng.randint(0, n - 1)
    r = rng.randint(l, n - 1)
    queries.append((l, r))
challenge._arr = list(arr)
challenge._queries = list(queries)
return {"arr": list(arr), "n": n, "queries": list(queries), "q": len(queries)}
''',
        "verify": '''
arr = challenge._arr
if not all(isinstance(v, int) for v in result):
    return False
expected = [min(arr[l:r + 1]) for l, r in challenge._queries]
return result == expected
''',
        "samples": [
            ("arr = [1, 3, 5, 7, 9, 11], n = 6, queries = [(1, 3), (0, 5)], q = 2", "[3, 1]"),
            ("arr = [5, 2, 8, 1, 9, 3], n = 6, queries = [(0, 2), (3, 5)], q = 2", "[2, 1]"),
        ],
        "hint": "Each tree[node] stores min of its range. For a query (l, r), if the node's range is fully inside, return its value; else recurse on children. Min of children is the answer.",
        "parents": ["segtree_02"],
        "children": ["segtree_06"],
    },

    # ============================================================
    # segtree_05: Range Update with Lazy Propagation
    # ============================================================
    {
        "id": "segtree_05",
        "name": "Range Update with Lazy Propagation",
        "category": "segment_tree",
        "difficulty": 6,
        "complexity": "O_N_LOG_N",
        "description": (
            "Build a sum-segment tree, then apply a sequence\n"
            "of range updates (add `val` to every element in\n"
            "[l, r]) using lazy propagation: when a node is\n"
            "fully inside the update range, add `val * width`\n"
            "to that node's sum and remember the pending\n"
            "update in a parallel `lazy` array (to be pushed\n"
            "down only when needed). Then for each query\n"
            "(l, r), return the range sum (with lazy tags\n"
            "pushed down on the way). O(log n) per op.\n"
            "Source: https://www.geeksforgeeks.org/dsa/lazy-propagation-in-segment-tree/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/lazy-propagation-in-segment-tree/",
        "params": ["arr", "n", "range_updates", "queries", "q"],
        "inputs": {
            "arr": "list of n integers (initial).",
            "n": "length of arr.",
            "range_updates": "list of (l, r, val) tuples: add val to arr[l..r].",
            "queries": "list of (l, r) range-sum queries (after all updates).",
            "q": "number of queries.",
        },
        "returns": "a list of q range sums after all range updates.",
        "solve": '''
def solve(arr, n, range_updates, queries, q):
    """Sum-segment tree with lazy-propagation range updates."""
    if n == 0:
        return [0] * q
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        build(2 * node, lo, mid)
        build(2 * node + 1, mid + 1, hi)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def apply(node, lo, hi, val):
        """Apply a pending update of `val` to this node."""
        tree[node] += val * (hi - lo + 1)
        lazy[node] += val

    def push(node, lo, hi):
        """Push pending lazy update down to children."""
        if lazy[node] != 0 and lo != hi:
            mid = (lo + hi) // 2
            apply(2 * node, lo, mid, lazy[node])
            apply(2 * node + 1, mid + 1, hi, lazy[node])
            lazy[node] = 0

    def update(node, lo, hi, l, r, val):
        if l > hi or r < lo:
            return
        if l <= lo and hi <= r:
            apply(node, lo, hi, val)
            return
        push(node, lo, hi)
        mid = (lo + hi) // 2
        update(2 * node, lo, mid, l, r, val)
        update(2 * node + 1, mid + 1, hi, l, r, val)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return 0
        if l <= lo and hi <= r:
            return tree[node]
        push(node, lo, hi)
        mid = (lo + hi) // 2
        return query(2 * node, lo, mid, l, r) + query(2 * node + 1, mid + 1, hi, l, r)

    build(1, 0, n - 1)
    for l, r, val in range_updates:
        update(1, 0, n - 1, l, r, val)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 10))
arr = [rng.randint(0, 20) for _ in range(n)]
n_u = max(1, min(2, n))
range_updates = []
for _ in range(n_u):
    l = rng.randint(0, n - 1)
    r = rng.randint(l, n - 1)
    val = rng.randint(-5, 10)
    range_updates.append((l, r, val))
n_q = max(1, min(3, n))
queries = []
for _ in range(n_q):
    l = rng.randint(0, n - 1)
    r = rng.randint(l, n - 1)
    queries.append((l, r))
challenge._arr = list(arr)
challenge._range_updates = list(range_updates)
challenge._queries = list(queries)
return {
    "arr": list(arr),
    "n": n,
    "range_updates": list(range_updates),
    "queries": list(queries),
    "q": len(queries),
}
''',
        "verify": '''
# Brute force: apply range updates to a working copy, then sum.
work = list(challenge._arr)
for l, r, val in challenge._range_updates:
    for i in range(l, r + 1):
        work[i] += val
expected = [sum(work[l:r + 1]) for l, r in challenge._queries]
return result == expected
''',
        "samples": [
            ("arr = [1, 3, 5, 7, 9, 11], n = 6, range_updates = [(1, 3, 5)], queries = [(0, 5)], q = 1", "[46] (= 1+8+10+12+9+11)"),
            ("arr = [1, 2, 3], n = 3, range_updates = [(0, 2, 10)], queries = [(0, 0), (1, 2), (0, 2)], q = 3", "[11, 25, 36]"),
        ],
        "hint": "Maintain a parallel lazy[] array. When updating a range, if the node is fully inside, add val * width to its sum and store val in lazy[node]. Push the lazy value down to children only when needed (on the way to a query or further update).",
        "parents": ["segtree_02"],
        "children": ["segtree_06"],
    },

    # ============================================================
    # segtree_06: Range Min + Range Update (Lazy on Min)
    # ============================================================
    {
        "id": "segtree_06",
        "name": "Range Min with Lazy Updates",
        "category": "segment_tree",
        "difficulty": 7,
        "complexity": "O_N_LOG_N",
        "description": (
            "Build a min-segment tree on arr. Apply a sequence\n"
            "of range updates (set every element in [l, r] to\n"
            "`val`) using lazy propagation (assignment, not\n"
            "addition). After all updates, for each query\n"
            "(l, r), return the minimum of the current arr\n"
            "values in that range. O(log n) per op.\n"
            "Source: https://www.geeksforgeeks.org/dsa/lazy-propagation-in-segment-tree-set-2/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/lazy-propagation-in-segment-tree-set-2/",
        "params": ["arr", "n", "range_updates", "queries", "q"],
        "inputs": {
            "arr": "list of n integers (initial).",
            "n": "length of arr.",
            "range_updates": "list of (l, r, val) tuples: set every arr[i] in [l, r] to val (assignment).",
            "queries": "list of (l, r) range-min queries (after all updates).",
            "q": "number of queries.",
        },
        "returns": "a list of q range minimums after all range assignments.",
        "solve": '''
def solve(arr, n, range_updates, queries, q):
    """Min-segment tree with lazy-assignment range updates."""
    if n == 0:
        return [0] * q
    INF_VAL = 10**9
    tree = [INF_VAL] * (4 * n)
    lazy = [None] * (4 * n)   # None = no pending assignment.

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        build(2 * node, lo, mid)
        build(2 * node + 1, mid + 1, hi)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def apply(node, lo, hi, val):
        """Apply a pending assignment of `val` to this node."""
        tree[node] = val
        lazy[node] = val

    def push(node, lo, hi):
        """Push pending assignment down to children."""
        if lazy[node] is not None and lo != hi:
            mid = (lo + hi) // 2
            apply(2 * node, lo, mid, lazy[node])
            apply(2 * node + 1, mid + 1, hi, lazy[node])
            lazy[node] = None

    def update(node, lo, hi, l, r, val):
        if l > hi or r < lo:
            return
        if l <= lo and hi <= r:
            apply(node, lo, hi, val)
            return
        push(node, lo, hi)
        mid = (lo + hi) // 2
        update(2 * node, lo, mid, l, r, val)
        update(2 * node + 1, mid + 1, hi, l, r, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return INF_VAL
        if l <= lo and hi <= r:
            return tree[node]
        push(node, lo, hi)
        mid = (lo + hi) // 2
        return min(query(2 * node, lo, mid, l, r),
                   query(2 * node + 1, mid + 1, hi, l, r))

    build(1, 0, n - 1)
    for l, r, val in range_updates:
        update(1, 0, n - 1, l, r, val)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 10))
arr = [rng.randint(0, 20) for _ in range(n)]
n_u = max(1, min(2, n))
range_updates = []
for _ in range(n_u):
    l = rng.randint(0, n - 1)
    r = rng.randint(l, n - 1)
    val = rng.randint(-5, 30)
    range_updates.append((l, r, val))
n_q = max(1, min(3, n))
queries = []
for _ in range(n_q):
    l = rng.randint(0, n - 1)
    r = rng.randint(l, n - 1)
    queries.append((l, r))
challenge._arr = list(arr)
challenge._range_updates = list(range_updates)
challenge._queries = list(queries)
return {
    "arr": list(arr),
    "n": n,
    "range_updates": list(range_updates),
    "queries": list(queries),
    "q": len(queries),
}
''',
        "verify": '''
work = list(challenge._arr)
for l, r, val in challenge._range_updates:
    for i in range(l, r + 1):
        work[i] = val
expected = [min(work[l:r + 1]) for l, r in challenge._queries]
return result == expected
''',
        "samples": [
            ("arr = [1, 3, 5, 7, 9, 11], n = 6, range_updates = [(1, 3, 5)], queries = [(0, 5)], q = 1", "[1] (after assignment [1,5,5,5,9,11], min is 1)"),
            ("arr = [5, 5, 5, 5, 5], n = 5, range_updates = [(1, 3, 0)], queries = [(0, 4)], q = 1", "[0] (after [5,0,0,0,5], min is 0)"),
        ],
        "hint": "Lazy ASSIGNMENT (not addition): when a node is fully inside the update range, set its min to val and store val in lazy[node]. Push the assignment down before recursing into children.",
        "parents": ["segtree_04", "segtree_05"],
        "children": [],
    },
]
