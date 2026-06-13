"""Binary Indexed Tree (Fenwick Tree).

Two problems from GFG's BIT catalog:

  01 Build BIT    - O(n log n) or O(n) build
  02 Prefix Sum   - O(log n) point updates + range sum queries

The BIT is an array of size n+1 where bit[i] stores the
cumulative sum of a range of arr. Updates are O(log n),
queries are O(log n).
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === fenwick_01: Build BIT ===

FENWICK_01_SOURCE = '''
def solve(arr, n):
    """Build a BIT (Fenwick tree) for arr.

    bit[i] = sum of arr[i - 2^k + 1 .. i] where k is the
    number of trailing zeros in i.
    """
    if n == 0:
        return []
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = arr[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    return bit
'''


def _setup_fenwick_build(challenge, n, seed):
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    arr = [rng.randint(0, 99) for _ in range(n)]
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_fenwick_build(challenge, result):
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    n = len(arr)
    if n == 0:
        return result == []
    if len(result) != n + 1:
        return False
    # Verify the BIT by checking prefix sums.
    bit = result
    cum = 0
    for i in range(1, n + 1):
        cum += arr[i - 1]
        s = 0
        k = i
        while k > 0:
            s += bit[k]
            k -= k & -k
        if s != cum:
            return False
    return True


# === fenwick_02: Range Sum Query with Updates ===

FENWICK_02_SOURCE = '''
def solve(arr, n, updates, queries, q):
    """Build a BIT, apply updates, then answer each range-sum query.

    updates is a list of (idx, val) where arr[idx] is SET
    to val (point update). queries is a list of (l, r) range
    sums. Return the list of range sums after all updates.
    """
    if n == 0:
        return [0] * q
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = arr[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]

    def update(i, delta):
        i += 1
        while i <= n:
            bit[i] += delta
            i += i & -i

    work = list(arr)
    for idx, val in updates:
        delta = val - work[idx]
        work[idx] = val
        update(idx, delta)

    out = []
    for l, r in queries:
        # prefix_sum(r) - prefix_sum(l-1)
        def prefix(i):
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        out.append(prefix(r) - (prefix(l - 1) if l > 0 else 0))
    return out
'''


def _setup_fenwick_query(challenge, n, seed):
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    arr = [rng.randint(0, 99) for _ in range(n)]
    n_u = max(0, min(2, n))
    updates = []
    for _ in range(n_u):
        idx = rng.randint(0, n - 1)
        val = rng.randint(0, 99)
        updates.append((idx, val))
    n_q = max(1, min(2, n))
    queries = []
    for _ in range(n_q):
        l = rng.randint(0, n - 1)
        r = rng.randint(l, n - 1)
        queries.append((l, r))
    challenge._arr = list(arr)
    challenge._updates = list(updates)
    challenge._queries = list(queries)
    return {"arr": list(arr), "n": n, "updates": list(updates), "queries": list(queries), "q": len(queries)}


def _verify_fenwick_query(challenge, result):
    if not isinstance(result, list):
        return False
    work = list(challenge._arr)
    for idx, val in challenge._updates:
        work[idx] = val
    expected = []
    for l, r in challenge._queries:
        expected.append(sum(work[l:r + 1]))
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="fenwick_01",
        name="Build Fenwick Tree",
        category="fenwick",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Build a Binary Indexed Tree (Fenwick tree) for arr.\n"
            "bit[i] = sum of arr[i - 2^k + 1 .. i] where k is the\n"
            "number of trailing zeros in i. O(n) build. After build,\n"
            "any prefix sum can be computed in O(log n).\n"
            "Source: https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/"
        ),
        source_url="https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers.",
            "n": "length of arr.",
        },
        returns="a list of length n+1 representing the BIT (1-indexed).",
        source=FENWICK_01_SOURCE,
        setup_fn=_setup_fenwick_build,
        verify_fn=_verify_fenwick_build,
        samples=[
            Sample("arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9], n = 12", "[0, 2, 3, 1, 7, 2, 5, 4, 14, 6, 13, 8, 9]"),
        ],
        hint="bit[i] = arr[i-1] for i in [1..n]. Then for i, j = i + (i & -i); if j <= n: bit[j] += bit[i].",
        parents=["segtree_01"],
        children=["fenwick_02"],
    ),
    AlgorithmSpec(
        id="fenwick_02",
        name="Range Sum Query (BIT)",
        category="fenwick",
        difficulty=3,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Build a BIT, apply a sequence of point updates, then\n"
            "answer each range-sum query by summing prefix sums.\n"
            "O(log n) per update and per query.\n"
            "Source: https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/"
        ),
        source_url="https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/",
        params=["arr", "n", "updates", "queries", "q"],
        inputs={
            "arr": "list of n integers (initial).",
            "n": "length of arr.",
            "updates": "list of (idx, val) tuples (set arr[idx] = val).",
            "queries": "list of (l, r) tuples (range sums).",
            "q": "number of queries.",
        },
        returns="a list of q range sums after applying the updates.",
        source=FENWICK_02_SOURCE,
        setup_fn=_setup_fenwick_query,
        verify_fn=_verify_fenwick_query,
        samples=[
            Sample("arr = [1, 3, 5], n = 3, updates = [(1, 8)], queries = [(0, 2)], q = 1", "[12]"),
        ],
        hint="Build BIT. For each update, add delta to bit[idx+1..] up the tree. For each query, sum bit[i] while i > 0.",
        parents=["fenwick_01"],
        children=[],
    ),
]
