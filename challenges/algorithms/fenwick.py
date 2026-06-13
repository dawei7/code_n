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


# === fenwick_03: 2D Fenwick Tree (Sub-matrix Sum) ===

FENWICK_03_SOURCE = '''
def solve(matrix, n, updates, queries, q):
    """2D BIT with point updates and sub-matrix sum queries.

    1-based BIT indexing internally (so cell (r, c) maps to
    BIT[r+1][c+1]).
    """
    if n == 0:
        return [0] * q
    # Build BIT.
    bit = [[0] * (n + 1) for _ in range(n + 1)]
    work = [row[:] for row in matrix]

    def update(r, c, delta):
        r += 1
        c += 1
        i = r
        while i <= n:
            j = c
            while j <= n:
                bit[i][j] += delta
                j += j & -j
            i += i & -i

    def prefix(r, c):
        # Sum over (0,0) .. (r,c) inclusive. Caller must clamp
        # r, c to -1 (which yields 0).
        if r < 0 or c < 0:
            return 0
        r += 1
        c += 1
        s = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                s += bit[i][j]
                j -= j & -j
            i -= i & -i
        return s

    # Build the BIT by inserting each cell's initial value.
    for r in range(n):
        for c in range(n):
            if matrix[r][c] != 0:
                update(r, c, matrix[r][c])

    # Apply updates.
    for r, c, delta in updates:
        work[r][c] += delta
        update(r, c, delta)

    # Answer queries.
    out = []
    for r1, c1, r2, c2 in queries:
        s = (prefix(r2, c2)
             - prefix(r1 - 1, c2)
             - prefix(r2, c1 - 1)
             + prefix(r1 - 1, c1 - 1))
        out.append(s)
    return out
'''

def _setup_fenwick_03(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 5))
    matrix = [[rng.randint(0, 9) for _ in range(n)] for _ in range(n)]
    n_u = max(0, min(2, n * n))
    updates = []
    for _ in range(n_u):
        r = rng.randint(0, n - 1)
        c = rng.randint(0, n - 1)
        delta = rng.randint(-5, 10)
        updates.append((r, c, delta))
    n_q = max(1, min(2, n * n))
    queries = []
    for _ in range(n_q):
        r1 = rng.randint(0, n - 1)
        r2 = rng.randint(r1, n - 1)
        c1 = rng.randint(0, n - 1)
        c2 = rng.randint(c1, n - 1)
        queries.append((r1, c1, r2, c2))
    challenge._matrix = [row[:] for row in matrix]
    challenge._updates = list(updates)
    challenge._queries = list(queries)
    return {
        "matrix": [row[:] for row in matrix],
        "n": n,
        "updates": list(updates),
        "queries": list(queries),
        "q": len(queries),
    }

def _verify_fenwick_03(challenge, result):
    # Brute force: apply updates, then for each query sum the submatrix.
    work = [row[:] for row in challenge._matrix]
    for r, c, delta in challenge._updates:
        work[r][c] += delta
    expected = []
    for r1, c1, r2, c2 in challenge._queries:
        s = 0
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                s += work[r][c]
        expected.append(s)
    return result == expected



# === fenwick_04: Range Update + Point Query (BIT) ===

FENWICK_04_SOURCE = '''
def solve(arr, n, range_updates, point_queries, q):
    """Range add + point query via single BIT.

    Seed the BIT with the initial arr values (so the point
    query at idx returns arr[idx] + accumulated deltas).
    """
    bit = [0] * (n + 2)

    def update(i, delta):
        i += 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i

    def prefix(i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # Initialize the BIT with the DIFF array, not the values.
    # For the "range update, point query" technique, the BIT
    # stores a difference array so that point query at idx
    # gives the current value at idx.
    if n > 0:
        update(0, arr[0])
        for i in range(1, n):
            update(i, arr[i] - arr[i - 1])
    # Apply range updates: diff array approach.
    for l, r, val in range_updates:
        update(l, val)
        if r + 1 < n:
            update(r + 1, -val)
    # Point queries: read prefix sum at each index.
    out = []
    for (idx,) in point_queries:
        out.append(prefix(idx))
    return out
'''

def _setup_fenwick_04(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    arr = [rng.randint(0, 20) for _ in range(n)]
    n_u = max(1, min(2, n))
    range_updates = []
    for _ in range(n_u):
        l = rng.randint(0, n - 1)
        r = rng.randint(l, n - 1)
        val = rng.randint(-5, 10)
        range_updates.append((l, r, val))
    n_q = max(1, min(3, n))
    point_queries = []
    for _ in range(n_q):
        idx = rng.randint(0, n - 1)
        point_queries.append((idx,))
    challenge._arr = list(arr)
    challenge._range_updates = list(range_updates)
    challenge._point_queries = list(point_queries)
    return {
        "arr": list(arr),
        "n": n,
        "range_updates": list(range_updates),
        "point_queries": list(point_queries),
        "q": len(point_queries),
    }

def _verify_fenwick_04(challenge, result):
    # Brute force: apply updates to a working copy, then read points.
    work = list(challenge._arr)
    for l, r, val in challenge._range_updates:
        for i in range(l, r + 1):
            work[i] += val
    expected = [work[idx] for (idx,) in challenge._point_queries]
    return result == expected



# === fenwick_05: Range Update + Range Query (BIT) ===

FENWICK_05_SOURCE = '''
def solve(arr, n, range_updates, range_queries, q):
    """Range add + range sum via two BITs.

    Seed both BITs with the initial arr values so the
    range sum reflects the actual current array.
    """
    INF = n + 5
    bit1 = [0] * (n + 2)
    bit2 = [0] * (n + 2)

    def update(bit, i, delta):
        i += 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i

    def prefix(bit, i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def range_update(l, r, val):
        update(bit1, l, val)
        if r + 1 < n:
            update(bit1, r + 1, -val)
        update(bit2, l, val * (l - 1))
        if r + 1 < n:
            update(bit2, r + 1, -val * r)

    def prefix_sum(x):
        # sum of [0, x]
        if x < 0:
            return 0
        return prefix(bit1, x) * x - prefix(bit2, x)

    # Initialize: each initial value is a point update (a
    # range update of length 1). This seeds both BITs so the
    # formula (bit1.prefix(x) * x - bit2.prefix(x)) yields
    # sum of arr[0..x] including the initial values.
    for i in range(n):
        range_update(i, i, arr[i])
    for l, r, val in range_updates:
        range_update(l, r, val)
    out = []
    for l, r in range_queries:
        out.append(prefix_sum(r) - prefix_sum(l - 1))
    return out
'''

def _setup_fenwick_05(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    arr = [rng.randint(0, 20) for _ in range(n)]
    n_u = max(1, min(2, n))
    range_updates = []
    for _ in range(n_u):
        l = rng.randint(0, n - 1)
        r = rng.randint(l, n - 1)
        val = rng.randint(-5, 10)
        range_updates.append((l, r, val))
    n_q = max(1, min(3, n))
    range_queries = []
    for _ in range(n_q):
        l = rng.randint(0, n - 1)
        r = rng.randint(l, n - 1)
        range_queries.append((l, r))
    challenge._arr = list(arr)
    challenge._range_updates = list(range_updates)
    challenge._range_queries = list(range_queries)
    return {
        "arr": list(arr),
        "n": n,
        "range_updates": list(range_updates),
        "range_queries": list(range_queries),
        "q": len(range_queries),
    }

def _verify_fenwick_05(challenge, result):
    work = list(challenge._arr)
    for l, r, val in challenge._range_updates:
        for i in range(l, r + 1):
            work[i] += val
    expected = [sum(work[l:r + 1]) for l, r in challenge._range_queries]
    return result == expected



# === fenwick_06: Count Inversions (BIT) ===

FENWICK_06_SOURCE = '''
def solve(arr, n):
    """Inversion count via BIT, with value compression."""
    if n <= 1:
        return 0
    # Compress arr to 1..n by rank order.
    sorted_unique = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    compressed = [rank[v] for v in arr]
    # BIT of size n (max compressed value is n).
    bit = [0] * (n + 2)
    inv = 0
    for i in range(n - 1, -1, -1):
        v = compressed[i]
        # prefix sum of bit up to v-1.
        j = v - 1
        s = 0
        while j > 0:
            s += bit[j]
            j -= j & -j
        inv += s
        # Add 1 at index v.
        j = v
        while j <= n:
            bit[j] += 1
            j += j & -j
    return inv
'''

def _setup_fenwick_06(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    # Mix of values (including repeats and negatives).
    arr = [rng.randint(-10, 10) for _ in range(n)]
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}

def _verify_fenwick_06(challenge, result):
    # Brute force inversion count.
    arr = challenge._arr
    n = len(arr)
    expected = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                expected += 1
    return result == expected



# === fenwick_07: K-th Smallest (Order-Statistic BIT) ===

FENWICK_07_SOURCE = '''
def solve(freq, n, k):
    """K-th smallest via order-statistic BIT (binary lifting)."""
    total = sum(freq)
    if k < 1 or k > total:
        return -1
    if n == 0:
        return -1
    # Build BIT.
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = freq[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    # Binary lifting: find largest idx with BIT.prefix(idx) < k.
    # The k-th smallest value is then idx + 1 (since the BIT
    # is 1-indexed and BIT[i] represents the count of value i).
    # The descent uses STRICT less-than: we take a step only
    # if bit[pos + bitmask] < (k - bit.prefix(pos)), so that
    # bit.prefix(pos) stays strictly less than k. The k-th
    # value is the smallest idx with prefix >= k, which is
    # (largest pos with prefix < k) + 1.
    idx = 0
    bitmask = 1
    while bitmask << 1 <= n:
        bitmask <<= 1
    remaining = k
    while bitmask > 0:
        nxt = idx + bitmask
        if nxt <= n and bit[nxt] < remaining:
            remaining -= bit[nxt]
            idx = nxt
        bitmask >>= 1
    return idx + 1
'''

def _setup_fenwick_07(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    # Frequencies summing to at least 4 (so we can ask for k in [1, total]).
    freq = [rng.randint(0, 3) for _ in range(n)]
    if sum(freq) == 0:
        freq[0] = 4
    challenge._freq = list(freq)
    # Pick a random k in [1, sum(freq)].
    challenge._k = rng.randint(1, sum(freq))
    return {"freq": list(freq), "n": n, "k": challenge._k}

def _verify_fenwick_07(challenge, result):
    # Brute force: flatten the multiset and return the k-th element.
    freq = challenge._freq
    k = challenge._k
    flat = []
    for v, c in enumerate(freq, start=1):
        flat.extend([v] * c)
    expected = flat[k - 1]   # 1-indexed
    return result == expected


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="fenwick_03",
        name="2D Fenwick Tree (Sub-matrix Sum)",
        category="fenwick",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Build a 2D Binary Indexed Tree on an n x n matrix,
            apply a sequence of point updates (add delta to a
            cell), then answer each sub-matrix sum query
            sum over the rectangle (r1, c1) .. (r2, c2)
            inclusive, using inclusion-exclusion over four
            2D prefix sums. O(log^2 n) per update and per
            query.
            Source: https://www.geeksforgeeks.org/dsa/two-dimensional-binary-indexed-tree-or-fenwick-tree/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/two-dimensional-binary-indexed-tree-or-fenwick-tree/",
        params=["matrix", "n", "updates", "queries", "q"],
        inputs={
            "matrix": "n x n list of lists of initial values.",
            "n": "matrix size (small in tests, n <= 5).",
            "updates": "list of (r, c, delta) tuples to add to cell (r, c).",
            "queries": "list of (r1, c1, r2, c2) sub-matrix queries.",
            "q": "number of queries.",
        },
        returns="a list of q sub-matrix sums after applying the updates.",
        source=FENWICK_03_SOURCE,
        setup_fn=_setup_fenwick_03,
        verify_fn=_verify_fenwick_03,
        samples=[
            Sample("matrix = [[1,2,3,4],[5,3,8,1],[4,6,7,5],[2,4,8,9]], n = 4, updates = [], queries = [(1,1,3,2)], q = 1", "[30]"),
            Sample("matrix = [[1,2,3,4],[5,3,8,1],[4,6,7,5],[2,4,8,9]], n = 4, updates = [(0,0,1),(1,1,-1)], queries = [(0,0,3,3)], q = 1", "[51] (= 55 + 1 - 5)"),
        ],
        hint="For each cell (i, j), walk i += i & -i and j += j & -j to add the cell's value. For prefix sum, walk i -= i & -i and j -= j & -j. Use inclusion-exclusion for sub-matrix.",
        parents=["fenwick_01"],
        children=["fenwick_04"],
    ),
    AlgorithmSpec(
        id="fenwick_04",
        name="Range Update + Point Query (BIT)",
        category="fenwick",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Maintain an array of n integers under repeated
            range-add updates (add `val` to every element in
            the range [l, r]) and point queries (return the
            current value at index `idx`). The classic BIT
            trick: maintain a single BIT, add `val` at index
            `l` and subtract `val` at index `r+1`. The point
            query at `idx` is then the prefix sum [0, idx].
            O(log n) per update and per query.
            Source: https://www.geeksforgeeks.org/dsa/binary-indexed-tree-range-update-point-query/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/binary-indexed-tree-range-update-point-query/",
        params=["arr", "n", "range_updates", "point_queries", "q"],
        inputs={
            "arr": "list of n initial values (informational only).",
            "n": "length of arr.",
            "range_updates": "list of (l, r, val) tuples: add val to arr[l..r].",
            "point_queries": "list of (idx,) tuples to read.",
            "q": "number of point queries.",
        },
        returns="a list of q point values after all range updates.",
        source=FENWICK_04_SOURCE,
        setup_fn=_setup_fenwick_04,
        verify_fn=_verify_fenwick_04,
        samples=[
            Sample("arr = [0,0,0,0,0], n = 5, range_updates = [(1,3,5)], point_queries = [(0,),(1,),(2,),(3,),(4,)], q = 5", "[0, 5, 5, 5, 0]"),
            Sample("arr = [1,3,5,7], n = 4, range_updates = [(0,2,10),(2,3,-3)], point_queries = [(0,),(1,),(2,),(3,)], q = 4", "[11, 13, 12, 4]"),
        ],
        hint="Add val at index l and -val at index r+1 in a BIT. Point query at idx is just the BIT prefix sum [0, idx].",
        parents=["fenwick_03"],
        children=["fenwick_05"],
    ),
    AlgorithmSpec(
        id="fenwick_05",
        name="Range Update + Range Query (BIT)",
        category="fenwick",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Maintain an array of n integers under repeated
            range-add updates and range-sum queries. Use two
            BITs: BIT1 holds a difference array; BIT2 holds a
            second auxiliary array. After a range update (l,
            r, val), update BIT1 with (l, +val, r+1, -val)
            and BIT2 with (l, val*(l-1), r+1, -val*r). The
            range sum [0, x] = prefix_BIT1(x) * x - prefix_BIT2(x).
            Then range sum [l, r] = sum(r) - sum(l-1). O(log n)
            per update and per query.
            Source: https://www.geeksforgeeks.org/dsa/binary-indexed-tree-range-update-range-queries/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/binary-indexed-tree-range-update-range-queries/",
        params=["arr", "n", "range_updates", "range_queries", "q"],
        inputs={
            "arr": "list of n initial values (informational only).",
            "n": "length of arr.",
            "range_updates": "list of (l, r, val) tuples: add val to arr[l..r].",
            "range_queries": "list of (l, r) tuples to read.",
            "q": "number of range queries.",
        },
        returns="a list of q range sums after all range updates.",
        source=FENWICK_05_SOURCE,
        setup_fn=_setup_fenwick_05,
        verify_fn=_verify_fenwick_05,
        samples=[
            Sample("arr = [0,0,0,0,0], n = 5, range_updates = [(1,3,2)], range_queries = [(0,4),(0,0),(1,3)], q = 3", "[6, 0, 6]"),
        ],
        hint="Two BITs: BIT1 holds the diff array, BIT2 holds val*(l-1) at l and -val*r at r+1. prefix_sum(x) = BIT1.prefix(x) * x - BIT2.prefix(x). Range sum is the difference of two prefix sums.",
        parents=["fenwick_04"],
        children=["fenwick_06"],
    ),
    AlgorithmSpec(
        id="fenwick_06",
        name="Count Inversions (BIT)",
        category="fenwick",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Count the number of inversions in an array: pairs
            (i, j) with i < j and arr[i] > arr[j]. Use a BIT
            on the value coordinate: first compress the values
            to 1..n (preserving rank order, so the result is
            unchanged). Traverse the array from right to left;
            for each arr[i], add prefix(arr[i] - 1) to the
            inversion count (this counts elements smaller than
            arr[i] that are to its right), then add 1 to the
            BIT at index arr[i]. O(n log n) total.
            Source: https://www.geeksforgeeks.org/dsa/inversion-count-in-array-using-bit/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/inversion-count-in-array-using-bit/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers (may be negative or repeated).",
            "n": "length of arr.",
        },
        returns="the inversion count as a non-negative int.",
        source=FENWICK_06_SOURCE,
        setup_fn=_setup_fenwick_06,
        verify_fn=_verify_fenwick_06,
        samples=[
            Sample("arr = [8, 4, 2, 1], n = 4", "6"),
            Sample("arr = [3, 1, 2], n = 3", "2"),
            Sample("arr = [1, 2, 3, 4], n = 4", "0 (sorted)"),
            Sample("arr = [4, 3, 2, 1], n = 4", "6 (reverse sorted)"),
        ],
        hint="Compress values to 1..n. Walk right to left; for each element, add (BIT prefix sum up to v-1) to the count of smaller-right elements, then update BIT at v with +1.",
        parents=["fenwick_05"],
        children=["fenwick_07"],
    ),
    AlgorithmSpec(
        id="fenwick_07",
        name="K-th Smallest (Order-Statistic BIT)",
        category="fenwick",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Given a frequency array freq[1..n] (how many times
            each value 1..n appears in a multiset), find the
            value of the k-th smallest element (1-indexed).
            Use an order-statistic BIT: build BIT[i] = freq[i],
            then find the smallest index `idx` such that
            BIT.prefix(idx) >= k, by binary lifting on the
            BIT's bit structure (descend the BIT starting from
            the highest set bit). O(log n) per query.
            Source: https://www.geeksforgeeks.org/dsa/order-statistic-tree-using-bit/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/order-statistic-tree-using-bit/",
        params=["freq", "n", "k"],
        inputs={
            "freq": "list of n non-negative integers (frequencies of values 1..n).",
            "n": "length of freq (small in tests, n <= 16).",
            "k": "1-indexed rank to find.",
        },
        returns="the value of the k-th smallest element (in [1, n]); -1 if k is out of range.",
        source=FENWICK_07_SOURCE,
        setup_fn=_setup_fenwick_07,
        verify_fn=_verify_fenwick_07,
        samples=[
            Sample("freq = [2, 1, 3, 0, 2], n = 5, k = 4", "2 (1,1,2,3,...)"),
            Sample("freq = [1, 2, 3], n = 3, k = 3", "2"),
            Sample("freq = [0, 0, 5], n = 3, k = 1", "3"),
        ],
        hint="Build a BIT from freq. Then binary-lift: starting from the highest power of 2 <= n, try to descend. Maintain 'remaining' = k; for each candidate step, if BIT[idx + step] <= remaining, take the step and subtract.",
        parents=["fenwick_06"],
        children=[],
    ),
])
