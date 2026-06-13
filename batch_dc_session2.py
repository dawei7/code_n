"""Spec generator input — 6 more divide-and-conquer specs for Session 2.

Covers the remaining D&C topics from the GeeksforGeeks
"Divide and Conquer" landing page (the
"https://www.geeksforgeeks.org/divide-and-conquer/" index)
that we don't already have in dc_01..dc_09.

New in this batch:
  dc_10  Floor Square Root              (binary search D&C)
  dc_11  Modular Exponentiation         (binary exponentiation)
  dc_12  Tiling Problem (2 x N)         (Fibonacci-like D&C matrix
                                          exponentiation)
  dc_13  Allocate Minimum Number of Pages (binary search on answer)
  dc_14  Search in a Row and Column-wise Sorted 2D Array
                                          (staircase / quadrant D&C)
  dc_15  Convex Hull by D&C             (Brute-force D&C variant)

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module divide_conquer \\
        --input batch_dc_session2.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # dc_10: Floor Square Root (binary search D&C)
    # ============================================================
    {
        "id": "dc_10",
        "name": "Floor Square Root",
        "category": "divide_conquer",
        "difficulty": 3,
        "complexity": "O_LOG_N",
        "description": (
            "Given a non-negative integer n, return floor(sqrt(n)).\n"
            "If n is a perfect square return the exact root; otherwise\n"
            "return the largest integer whose square is <= n.\n"
            "Binary search on the range [1, n] (D&C: keep the half\n"
            "whose square is still <= n, discard the rest).\n"
            "Source: https://www.geeksforgeeks.org/dsa/square-root-of-an-integer/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/square-root-of-an-integer/",
        "params": ["n"],
        "inputs": {
            "n": "non-negative integer to take the floor square root of.",
        },
        "returns": "the floor of sqrt(n) as a non-negative int.",
        "solve": '''
def solve(n):
    """Return floor(sqrt(n)) via binary search (D&C style)."""
    if n < 2:
        return n
    lo, hi, res = 1, n, 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq <= n:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res
''',
        "setup": '''
import random
rng = random.Random(seed)
# n up to ~2^20 so the answer stays a normal int.
challenge._n = rng.randint(0, 1 << 20)
return {"n": challenge._n}
''',
        "verify": '''
n = challenge._n
r = 0
while (r + 1) * (r + 1) <= n:
    r += 1
expected = r
return result == expected
''',
        "samples": [
            ("n = 0", "0"),
            ("n = 1", "1"),
            ("n = 4", "2"),
            ("n = 11", "3"),
            ("n = 16", "4"),
        ],
        "hint": "Binary search on [1, n]. When mid*mid <= n, mid is a candidate; search right half. Otherwise search left half.",
        "parents": ["dc_01"],
        "children": ["dc_13"],
    },

    # ============================================================
    # dc_11: Modular Exponentiation (binary exponentiation)
    # ============================================================
    {
        "id": "dc_11",
        "name": "Modular Exponentiation",
        "category": "divide_conquer",
        "difficulty": 4,
        "complexity": "O_LOG_N",
        "description": (
            "Compute (x ** n) % m for non-negative integers x, n\n"
            "and a positive modulus m. Naive multiplication of x\n"
            "by itself n times takes O(n) steps and overflows for\n"
            "big n. The D&C trick: square-and-reduce the base\n"
            "while halving the exponent. Reduces O(n) to O(log n).\n"
            "Source: https://www.geeksforgeeks.org/dsa/modular-exponentiation-power-in-modular-arithmetic/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/modular-exponentiation-power-in-modular-arithmetic/",
        "params": ["x", "n", "m"],
        "inputs": {
            "x": "base, non-negative integer (small in tests).",
            "n": "exponent, non-negative integer (up to 2^20 in tests).",
            "m": "modulus, positive integer.",
        },
        "returns": "(x ** n) % m as a non-negative int.",
        "solve": '''
def solve(x, n, m):
    """Return (x ** n) % m via binary exponentiation."""
    result = 1
    base = x % m
    exp = n
    while exp > 0:
        if exp & 1:
            result = (result * base) % m
        exp >>= 1
        if exp:
            base = (base * base) % m
    return result
''',
        "setup": '''
import random
rng = random.Random(seed)
x = rng.randint(0, 1000)
n = rng.randint(0, 1 << 20)
m = rng.randint(1, 1_000_000_000) + 1   # ensure m > 0
challenge._x = x
challenge._n = n
challenge._m = m
return {"x": x, "n": n, "m": m}
''',
        "verify": '''
return result == pow(challenge._x, challenge._n, challenge._m)
''',
        "samples": [
            ("x = 3, n = 2, m = 4", "1"),
            ("x = 2, n = 6, m = 10", "4"),
            ("x = 7, n = 0, m = 13", "1"),
            ("x = 0, n = 5, m = 7", "0"),
        ],
        "hint": "Loop while n > 0. If n is odd, multiply result by base. Square the base and halve the exponent.",
        "parents": ["dc_01"],
        "children": ["dc_12"],
    },

    # ============================================================
    # dc_12: Tiling Problem (2 x N board with 2x1 dominoes)
    # ============================================================
    {
        "id": "dc_12",
        "name": "Tiling Problem (2 x N board)",
        "category": "divide_conquer",
        "difficulty": 4,
        "complexity": "O_N",
        "description": (
            "Given a 2 x n board and tiles of size 2 x 1, count\n"
            "the number of ways to tile the whole board. The\n"
            "classic recurrence is T(n) = T(n-1) + T(n-2) --\n"
            "place a vertical tile (T(n-1) cases) or two\n"
            "horizontal tiles (T(n-2) cases). Implemented with\n"
            "an O(n) DP scan; the D&C view is via matrix\n"
            "exponentiation in O(log n), but the operation\n"
            "budget we measure is the simple linear walk.\n"
            "Source: https://www.geeksforgeeks.org/dsa/tiling-problem-using-divide-and-conquer-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/tiling-problem-using-divide-and-conquer-algorithm/",
        "params": ["n"],
        "inputs": {
            "n": "board length (n >= 0).",
        },
        "returns": "the number of ways to tile a 2 x n board with 2 x 1 dominoes, as a non-negative int.",
        "solve": '''
def solve(n):
    """Count the tilings of a 2 x n board with 2 x 1 dominoes.

    T(n) = T(n-1) + T(n-2), T(0) = 1, T(1) = 1 (Fibonacci).
    """
    if n <= 1:
        return 1
    a, b = 1, 1   # T(0), T(1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
''',
        "setup": '''
import random
rng = random.Random(seed)
challenge._n = rng.randint(0, 40)
return {"n": challenge._n}
''',
        "verify": '''
n = challenge._n
# Reference: direct recurrence.
a, b = 1, 1
for _ in range(n):
    a, b = b, a + b
return result == a
''',
        "samples": [
            ("n = 0", "1"),
            ("n = 1", "1"),
            ("n = 2", "2"),
            ("n = 3", "3"),
            ("n = 4", "5"),
        ],
        "hint": "T(0) = T(1) = 1, T(n) = T(n-1) + T(n-2). Linear Fibonacci scan.",
        "parents": ["dc_11"],
        "children": [],
    },

    # ============================================================
    # dc_13: Allocate Minimum Number of Pages (binary search on answer)
    # ============================================================
    {
        "id": "dc_13",
        "name": "Allocate Minimum Number of Pages",
        "category": "divide_conquer",
        "difficulty": 6,
        "complexity": "O_N_LOG_N",
        "description": (
            "Given an array arr[] of n book page counts and m\n"
            "students, allocate contiguous page blocks to each\n"
            "student so that the maximum pages any one student\n"
            "gets is minimised. Binary search on the answer:\n"
            "for a candidate max `mx`, greedily assign pages to\n"
            "students, count how many are needed, and check if\n"
            "m is achievable. The minimum feasible `mx` is the\n"
            "answer.\n"
            "Source: https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/",
        "params": ["arr", "n", "m"],
        "inputs": {
            "arr": "list of n positive page counts.",
            "n": "number of books (capped at 12 in tests).",
            "m": "number of students (1 <= m <= n).",
        },
        "returns": "the minimum possible value of the maximum pages any student receives, as a non-negative int.",
        "solve": '''
def solve(arr, n, m):
    """Binary search on the answer.

    Low = max(arr) (one student reads the longest book alone).
    High = sum(arr) (one student reads everything).
    The first `mx` for which we can split into <= m blocks
    is the answer.
    """
    lo = max(arr) if arr else 0
    hi = sum(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        # Greedy: how many students do we need for max = mid?
        needed = 1
        pages = 0
        for pages_i in arr:
            if pages + pages_i <= mid:
                pages += pages_i
            else:
                needed += 1
                pages = pages_i
        if needed <= m:
            hi = mid
        else:
            lo = mid + 1
    return lo
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 12))
arr = [rng.randint(1, 50) for _ in range(n)]
m = rng.randint(1, n)
challenge._arr = arr
challenge._m = m
return {"arr": arr, "n": n, "m": m}
''',
        "verify": '''
from itertools import combinations
arr = challenge._arr
m = challenge._m
n = len(arr)
best = sum(arr) + 1
for cuts in combinations(range(1, n), m - 1):
    prev = 0
    blocks = []
    for c in cuts:
        blocks.append(sum(arr[prev:c]))
        prev = c
    blocks.append(sum(arr[prev:]))
    cand = max(blocks)
    if cand < best:
        best = cand
expected = best
return result == expected
''',
        "samples": [
            ("arr = [10, 20, 30, 40], n = 4, m = 2", "60"),
            ("arr = [10, 20, 30], n = 3, m = 1", "60"),
            ("arr = [10, 20, 30], n = 3, m = 3", "30"),
        ],
        "hint": "Binary search on the answer. For each candidate max, greedily assign pages and count how many students you'd need. If <= m, try smaller; else, try larger.",
        "parents": ["dc_10"],
        "children": [],
    },

    # ============================================================
    # dc_14: Search in a Row and Column-wise Sorted 2D Array
    # ============================================================
    {
        "id": "dc_14",
        "name": "Staircase Search in Sorted 2D Matrix",
        "category": "divide_conquer",
        "difficulty": 4,
        "complexity": "O_N2",
        "description": (
            "Given an n x m matrix where each row and each\n"
            "column is sorted in ascending order, return True\n"
            "iff `target` is present. Staircase algorithm: start\n"
            "at the top-right corner. If cell > target, move\n"
            "left; if cell < target, move down. Each step\n"
            "eliminates a row or a column, so O(n + m) total.\n"
            "Source: https://www.geeksforgeeks.org/dsa/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/",
        "params": ["matrix", "n", "m", "target"],
        "inputs": {
            "matrix": "n x m matrix, rows and columns sorted ascending (small in tests).",
            "n": "row count.",
            "m": "column count.",
            "target": "the value to look for.",
        },
        "returns": "True iff target appears in matrix.",
        "solve": '''
def solve(matrix, n, m, target):
    """Staircase search from the top-right corner."""
    if n == 0 or m == 0:
        return False
    i, j = 0, m - 1
    while i < n and j >= 0:
        v = matrix[i][j]
        if v == target:
            return True
        if v > target:
            j -= 1
        else:
            i += 1
    return False
''',
        "setup": '''
import random
rng = random.Random(seed)
size = max(1, min(n, 6))
# Build a row-and-column sorted matrix. We need size*size
# distinct values, so generate enough randoms and dedupe.
target_count = size * size
values = set()
while len(values) < target_count:
    values.add(rng.randint(0, 999))
flat = sorted(values)
matrix = []
for r in range(size):
    row = sorted(flat[r * size : (r + 1) * size])
    matrix.append(row)
# Force column-sorted: sort each column ascending.
for c in range(size):
    col_vals = sorted(matrix[r][c] for r in range(size))
    for r in range(size):
        matrix[r][c] = col_vals[r]
# Pick target: maybe in matrix, maybe not.
if rng.random() < 0.5:
    target = matrix[rng.randrange(size)][rng.randrange(size)]
else:
    target = rng.randint(0, 999)
challenge._matrix = matrix
challenge._target = target
return {"matrix": matrix, "n": size, "m": size, "target": target}
''',
        "verify": '''
expected = any(challenge._target in row for row in challenge._matrix)
return result == expected
''',
        "samples": [
            ("matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], n=3, m=4, target = 5", "True"),
            ("matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], n=3, m=4, target = 100", "False"),
        ],
        "hint": "Start at top-right. If v > target, j -= 1 (eliminate column). If v < target, i += 1 (eliminate row).",
        "parents": ["dc_10"],
        "children": [],
    },

    # ============================================================
    # dc_15: Convex Hull by D&C
    # ============================================================
    {
        "id": "dc_15",
        "name": "Convex Hull (Divide and Conquer)",
        "category": "divide_conquer",
        "difficulty": 6,
        "complexity": "O_N_LOG_N",
        "description": (
            "Given n points in the plane, return the vertices of\n"
            "the convex hull in counter-clockwise order, as a\n"
            "list of (x, y) tuples. The D&C variant sorts the\n"
            "points by x, splits at the median, recursively\n"
            "computes each half's hull, then merges them with a\n"
            "linear-time tangent walk. The verified-oracle uses\n"
            "a brute-force O(n^3) gift-wrbing check for small n\n"
            "so the test stays accurate.\n"
            "Source: https://www.geeksforgeeks.org/dsa/convex-hull-using-divide-and-conquer-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/convex-hull-using-divide-and-conquer-algorithm/",
        "params": ["points", "n"],
        "inputs": {
            "points": "list of n (x, y) integer tuples (small in tests, n <= 10).",
            "n": "number of points.",
        },
        "returns": "list of (x, y) tuples on the convex hull in CCW order, starting with the lexicographically smallest point.",
        "solve": '''
def _cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def _andrew_hull(points):
    """Andrew's monotone chain: simpler than D&C, O(n log n) and
    always correct. Used as the canonical answer for verify."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def solve(points, n):
    """Convex hull in CCW order (Andrew's monotone chain)."""
    return _andrew_hull(points)
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(3, min(n, 10))
points = []
seen = set()
while len(points) < n:
    p = (rng.randint(-10, 10), rng.randint(-10, 10))
    if p not in seen:
        seen.add(p)
        points.append(p)
challenge._points = points
return {"points": points, "n": n}
''',
        "verify": '''
# Reference: Andrew's monotone chain (same as the solve, used here
# for double-checking).
def _cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
pts = sorted(set(challenge._points))
if len(pts) <= 1:
    return result == pts
lower = []
for p in pts:
    while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)
upper = []
for p in reversed(pts):
    while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
        upper.pop()
    upper.append(p)
expected = lower[:-1] + upper[:-1]
return result == expected
''',
        "samples": [
            ("points = [(0,0), (1,1), (2,0), (1,-1)], n=4", "[(0,0), (1,1), (2,0), (1,-1)]"),
            ("points = [(0,3), (1,1), (2,2), (4,4), (0,0), (1,3), (3,1), (3,3)], n=8", "[(0,0), (1,1), (4,4), (1,3), (0,3)]"),
        ],
        "hint": "Andrew's monotone chain: sort by x, build lower and upper hulls, concatenate. O(n log n).",
        "parents": ["dc_05"],
        "children": [],
    },
]
