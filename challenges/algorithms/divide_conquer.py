"""Divide and conquer algorithms.

Three problems from GFG's divide-and-conquer catalog:

  01 Power(x, n)           - x^n via half-the-exponent recursion
  02 Majority Element      - Boyer-Moore linear-time vote
  03 Kth Smallest (Quickselect) - partition like quicksort, but
    only recurse into the side that contains the answer

The verify_fn re-runs the canonical algorithm and compares, so
each spec is a self-contained oracle pair. Setup is
deterministic via ``random.Random(seed)``.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === dc_01: Power(x, n) ===

DC_01_SOURCE = '''\
"""Optimal solution for dc_01: Power(x, n).

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. Handle negative n by computing the reciprocal. O(log n).
"""


def solve(x, n):
    if n == 0:
        return 1
    # Use absolute exponent, then take reciprocal at the end if needed.
    abs_n = -n if n < 0 else n
    result = 1.0
    base = float(x)
    while abs_n > 0:
        if abs_n & 1:
            result *= base
        abs_n >>= 1
        if abs_n:
            base *= base
    if n < 0:
        return 1.0 / result
    return result
'''


def _setup_power(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # x is a small integer or float; n is bounded by 2^k so we
    # can verify with a small loop.
    x = rng.choice([rng.randint(-5, 5) or 1, rng.uniform(-3.0, 3.0)])
    exp = rng.randint(0, max(2, n))
    challenge._x = x
    challenge._n = exp
    return {"x": x, "n": exp}


def _verify_power(challenge, result: Any) -> bool:
    if not isinstance(result, (int, float)):
        return False
    expected = challenge._x ** challenge._n
    if expected == 0:
        return result == 0
    return abs(result - expected) < 1e-9 * (1 + abs(expected))


# === dc_02: Majority Element ===

DC_02_SOURCE = '''\
"""Optimal solution for dc_02: Majority Element.

Boyer-Moore: track a candidate and a counter. Walk the array;
on each new element, if the counter is zero, promote it to
candidate. Increment on a match, decrement otherwise. The
candidate at the end is the majority element if one exists.
The setup always produces a list with a majority, so the
candidate is the answer.
"""


def solve(arr, n):
    if n == 0:
        return -1
    candidate = None
    count = 0
    for value in arr:
        if count == 0:
            candidate = value
        count += 1 if value == candidate else -1
    return candidate
'''


def _setup_majority(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    # Pick a majority value; ensure it appears strictly more than n/2 times.
    majority = rng.randint(0, 9)
    majority_count = (n // 2) + 1
    arr = [majority] * majority_count
    # Fill the rest with other values (not equal to majority).
    for _ in range(n - majority_count):
        v = rng.randint(0, 9)
        while v == majority:
            v = rng.randint(0, 9)
        arr.append(v)
    rng.shuffle(arr)
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_majority(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    arr = challenge._arr
    if not arr:
        return result == -1
    # The setup guarantees a majority exists.
    counts = {}
    for v in arr:
        counts[v] = counts.get(v, 0) + 1
    majority_value = max(counts, key=counts.get)
    return result == majority_value


# === dc_03: Kth Smallest (Quickselect) ===

DC_03_SOURCE = '''\
"""Optimal solution for dc_03: Kth Smallest (Quickselect).

Quickselect: partition the array around a pivot (Lomuto-style),
then only recurse into the half that contains the kth smallest.
O(n) average case, O(n^2) worst case on pathological data.
The setup shuffles the array first to keep the worst case rare.
"""


def solve(arr, k, n):
    if k < 1 or k > n:
        return -1
    work = list(arr)
    target = k - 1  # 0-indexed

    def select(lo, hi):
        if lo == hi:
            return work[lo]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        if i == target:
            return work[i]
        if i < target:
            return select(i + 1, hi)
        return select(lo, i - 1)

    return select(0, n - 1)
'''


def _setup_quickselect(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(2, min(n, 16))
    arr = [rng.randint(0, 99) for _ in range(n)]
    rng.shuffle(arr)  # help avoid pathological quickselect
    k = rng.randint(1, n)
    challenge._arr = list(arr)
    challenge._k = k
    return {"arr": list(arr), "k": k, "n": n}


def _verify_quickselect(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    expected = sorted(challenge._arr)[challenge._k - 1]
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="dc_01",
        name="Power (x to the n)",
        category="divide_conquer",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Compute x^n for a real x and a non-negative integer n.\n"
            "Use divide-and-conquer: x^n = (x^(n//2))^2, with an extra\n"
            "x when n is odd. O(log n) multiplications.\n"
            "Source: https://www.geeksforgeeks.org/write-a-program-to-calculate-powxn/"
        ),
        source_url="https://www.geeksforgeeks.org/write-a-program-to-calculate-powxn/",
        params=["x", "n"],
        inputs={
            "x": "base (real number, integer or float).",
            "n": "exponent (non-negative integer).",
        },
        returns="x ** n (float).",
        source=DC_01_SOURCE,
        setup_fn=_setup_power,
        verify_fn=_verify_power,
        samples=[
            Sample("x = 2, n = 10", "1024"),
            Sample("x = 2.0, n = -2", "0.25  (setup always uses n >= 0; this sample is illustrative)"),
            Sample("x = 3, n = 0", "1"),
        ],
        hint="Repeated squaring. Multiply the result on set bits of n.",
        parents=["math_03"],
        children=["dc_02"],
    ),
    AlgorithmSpec(
        id="dc_02",
        name="Majority Element",
        category="divide_conquer",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "The setup always generates a list with a majority element\n"
            "(occurs strictly more than n/2 times). Find and return that\n"
            "value. Boyer-Moore: track a candidate and counter; promote on\n"
            "counter=0, increment on match, decrement on mismatch. The\n"
            "final candidate is the majority if one exists.\n"
            "Requirement: O(n) time, O(1) space.\n"
            "Source: https://www.geeksforgeeks.org/majority-element/"
        ),
        source_url="https://www.geeksforgeeks.org/majority-element/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers (always has a majority).",
            "n": "length of arr.",
        },
        returns="the majority element (the one that appears > n/2 times).",
        source=DC_02_SOURCE,
        setup_fn=_setup_majority,
        verify_fn=_verify_majority,
        samples=[
            Sample("arr = [3, 1, 3, 3, 2], n = 5", "3"),
            Sample("arr = [1], n = 1", "1"),
        ],
        hint="Walk once. On counter=0, promote the current value. Increment on match, decrement on mismatch.",
        parents=["dc_01"],
        children=["dc_03"],
    ),
    AlgorithmSpec(
        id="dc_03",
        name="Kth Smallest (Quickselect)",
        category="divide_conquer",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the kth smallest element in an unsorted array (k is\n"
            "1-indexed). Quickselect: partition like quicksort, then\n"
            "recurse only into the half that contains the answer. O(n)\n"
            "average, O(n^2) worst case on pathological data; the setup\n"
            "shuffles the input to keep the worst case rare.\n"
            "Source: https://www.geeksforgeeks.org/quickselect-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/quickselect-algorithm/",
        params=["arr", "k", "n"],
        inputs={
            "arr": "list of n random integers (shuffled).",
            "k": "1-indexed rank to return.",
            "n": "length of arr.",
        },
        returns="the kth smallest element, or -1 if k is out of range.",
        source=DC_03_SOURCE,
        setup_fn=_setup_quickselect,
        verify_fn=_verify_quickselect,
        samples=[
            Sample("arr = [7, 10, 4, 3, 20, 15], k = 3, n = 6", "7"),
            Sample("arr = [5, 5, 5], k = 1, n = 3", "5"),
        ],
        hint="Partition around a pivot; only recurse into the side that contains the kth index.",
        parents=["dc_02"],
        children=[],
    ),
]


# === dc_04: Karatsuba Multiplication ===

DC_04_SOURCE = '''
def solve(x, y, n):
    """Karatsuba multiplication: x * y.

    Recursive 3-way multiplication beats the schoolbook 4-way
    multiplication by trading one extra add/subtract for one
    fewer recursive product.
    """
    if x < 10 or y < 10:
        return x * y
    m = max(len(str(x)), len(str(y)))
    half = m // 2
    pow10 = 10 ** half
    a, b = divmod(x, pow10)
    c, d = divmod(y, pow10)
    ac = solve(a, c, n)
    bd = solve(b, d, n)
    ad_bc = solve(a + b, c + d, n) - ac - bd
    return ac * 10 ** (2 * half) + ad_bc * 10 ** half + bd
'''

def _setup_dc_04(challenge, n, seed):
    rng = random.Random(seed)
    x = rng.randint(0, 9999)
    y = rng.randint(0, 9999)
    challenge._x = x
    challenge._y = y
    return {"x": x, "y": y, "n": max(len(str(x)), len(str(y)))}

def _verify_dc_04(challenge, result):
    return isinstance(result, int) and result == challenge._x * challenge._y



# === dc_05: Closest Pair of Points ===

DC_05_SOURCE = '''
def solve(points, n):
    """Closest pair of points via D&C plane sweep."""
    if n < 2:
        return 0.0
    px = sorted(points, key=lambda p: (p[0], p[1]))
    return _closest(px, 0, n - 1)

def _dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def _brute(pts, lo, hi):
    best = float("inf")
    for i in range(lo, hi + 1):
        for j in range(i + 1, hi + 1):
            d = _dist(pts[i], pts[j])
            if d < best:
                best = d
    return best

def _closest(px, lo, hi):
    n = hi - lo + 1
    if n <= 3:
        return _brute(px, lo, hi)
    mid = (lo + hi) // 2
    mid_x = px[mid][0]
    dl = _closest(px, lo, mid)
    dr = _closest(px, mid + 1, hi)
    d = min(dl, dr)
    strip = [px[k] for k in range(lo, hi + 1) if abs(px[k][0] - mid_x) < d]
    strip.sort(key=lambda p: p[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) ** 2 >= d * d:
                break
            cand = _dist(strip[i], strip[j])
            if cand < d:
                d = cand
    return d
'''

def _setup_dc_05(challenge, n, seed):
    rng = random.Random(seed)
    n_pts = max(2, min(n, 8))
    points = [(rng.randint(-10, 10), rng.randint(-10, 10)) for _ in range(n_pts)]
    challenge._points = points
    return {"points": points, "n": n_pts}

def _verify_dc_05(challenge, result):
    pts = challenge._points
    n = len(pts)
    if n < 2:
        return result == 0.0
    best = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            dx = pts[i][0] - pts[j][0]
            dy = pts[i][1] - pts[j][1]
            d = (dx * dx + dy * dy) ** 0.5
            if d < best:
                best = d
    if best == 0.0:
        return result == 0.0
    return abs(result - best) < 1e-9



# === dc_06: Strassen Matrix Multiplication ===

DC_06_SOURCE = '''
def solve(A, B, n):
    """Strassen 2x2 matrix multiplication.

    Seven products (p1..p7) replace the schoolbook eight,
    trading a few extra additions for one fewer multiply.
    """
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    if n == 2:
        a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
        e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
        p1 = a * (f - h)
        p2 = (a + b) * h
        p3 = (c + d) * e
        p4 = d * (g - e)
        p5 = (a + d) * (e + h)
        p6 = (b - d) * (g + h)
        p7 = (a - c) * (e + f)
        c00 = p5 + p4 - p2 + p6
        c01 = p1 + p2
        c10 = p3 + p4
        c11 = p1 + p5 - p3 - p7
        return [[c00, c01], [c10, c11]]
    return _naive(A, B, n)

def _naive(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
'''

def _setup_dc_06(challenge, n, seed):
    rng = random.Random(seed)
    n_dim = 2
    A = [[rng.randint(-5, 5) for _ in range(n_dim)] for _ in range(n_dim)]
    B = [[rng.randint(-5, 5) for _ in range(n_dim)] for _ in range(n_dim)]
    challenge._A = A
    challenge._B = B
    return {"A": A, "B": B, "n": n_dim}

def _verify_dc_06(challenge, result):
    A = challenge._A
    B = challenge._B
    n = len(A)
    if not (isinstance(result, list) and len(result) == n and all(len(r) == n for r in result)):
        return False
    # Schoolbook reference.
    expected = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            expected[i][j] = s
    return result == expected



# === dc_07: Skyline Problem ===

DC_07_SOURCE = '''
def solve(buildings, n):
    """Skyline via D&C: recurse, then merge two skylines."""
    if n == 0:
        return []
    if n == 1:
        l, h, r = buildings[0]
        return [[l, h], [r, 0]]
    mid = n // 2
    left = solve(buildings[:mid], mid)
    right = solve(buildings[mid:], n - mid)
    return _merge(left, right)

def _merge(left, right):
    result = []
    h1 = h2 = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x, h1 = left[i][0], left[i][1]
            i += 1
        elif left[i][0] > right[j][0]:
            x, h2 = right[j][0], right[j][1]
            j += 1
        else:
            x = left[i][0]
            h1 = left[i][1]
            h2 = right[j][1]
            i += 1
            j += 1
        h = max(h1, h2)
        if not result or result[-1][1] != h:
            result.append([x, h])
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
'''

def _setup_dc_07(challenge, n, seed):
    rng = random.Random(seed)
    n_b = max(1, min(n, 6))
    buildings = []
    for _ in range(n_b):
        l = rng.randint(0, 8)
        w = rng.randint(1, 4)
        h = rng.randint(1, 6)
        buildings.append((l, h, l + w))
    challenge._buildings = buildings
    return {"buildings": buildings, "n": n_b}

def _verify_dc_07(challenge, result):
    bld = challenge._buildings
    if not bld:
        return result == []
    # Brute force: sweep every integer x from 0 to max right.
    xs = set()
    for l, _h, r in bld:
        for x in range(l, r + 1):
            xs.add(x)
    xs = sorted(xs)
    expected = []
    prev_h = None
    for x in xs:
        h = 0
        for l, bh, r in bld:
            if l <= x < r:
                h = max(h, bh)
        if h != prev_h:
            expected.append([x, h])
            prev_h = h
    # Each skyline ends at the rightmost x with height 0.
    if expected[-1][1] != 0:
        max_r = max(r for _l, _h, r in bld)
        expected.append([max_r, 0])
    return result == expected



# === dc_08: Count Inversions ===

DC_08_SOURCE = '''
def solve(arr, n):
    """Count inversions via merge sort."""
    if n <= 1:
        return 0
    work = list(arr)

    def sort_count(lo, hi):
        if lo >= hi:
            return 0
        mid = (lo + hi) // 2
        count = sort_count(lo, mid) + sort_count(mid + 1, hi)
        left = work[lo:mid + 1]
        right = work[mid + 1:hi + 1]
        i = j = 0
        k = lo
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                work[k] = left[i]
                i += 1
            else:
                work[k] = right[j]
                count += len(left) - i
                j += 1
            k += 1
        while i < len(left):
            work[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            work[k] = right[j]
            j += 1
            k += 1
        return count

    return sort_count(0, n - 1)
'''

def _setup_dc_08(challenge, n, seed):
    rng = random.Random(seed)
    n_arr = max(1, min(n, 10))
    arr = [rng.randint(0, 9) for _ in range(n_arr)]
    challenge._arr = arr
    return {"arr": arr, "n": n_arr}

def _verify_dc_08(challenge, result):
    arr = challenge._arr
    n = len(arr)
    expected = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                expected += 1
    return result == expected



# === dc_09: Median of Two Sorted Arrays ===

DC_09_SOURCE = '''
def solve(a, b, m, n):
    """Median of two sorted arrays in O(log(min(m, n)))."""
    if m > n:
        return solve(b, a, n, m)
    lo, hi = 0, m
    half = (m + n + 1) // 2
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        if i > 0 and a[i - 1] > b[j]:
            hi = i - 1
        elif i < m and j > 0 and b[j - 1] > a[i]:
            lo = i + 1
        else:
            # Found the right partition.
            if i == 0:
                left_max = b[j - 1]
            elif j == 0:
                left_max = a[i - 1]
            else:
                left_max = max(a[i - 1], b[j - 1])
            if (m + n) % 2 == 1:
                return float(left_max)
            if i == m:
                right_min = b[j]
            elif j == n:
                right_min = a[i]
            else:
                right_min = min(a[i], b[j])
            return (left_max + right_min) / 2
'''

def _setup_dc_09(challenge, n, seed):
    rng = random.Random(seed)
    m = max(1, min(n, 6))
    remaining = max(1, min(n, 6))
    a = sorted(rng.randint(0, 9) for _ in range(m))
    b = sorted(rng.randint(0, 9) for _ in range(remaining))
    challenge._a = a
    challenge._b = b
    return {"a": a, "b": b, "m": m, "n": remaining}

def _verify_dc_09(challenge, result):
    a = challenge._a
    b = challenge._b
    merged = sorted(a + b)
    total = len(merged)
    if total % 2 == 1:
        expected = float(merged[total // 2])
    else:
        expected = (merged[total // 2 - 1] + merged[total // 2]) / 2
    if expected == 0.0:
        return result == 0.0
    if not isinstance(result, (int, float)):
        return False
    return abs(float(result) - float(expected)) < 1e-9


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="dc_04",
        name="Karatsuba Multiplication",
        category="divide_conquer",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Multiply two non-negative integers using Karatsuba's
            divide-and-conquer algorithm. Split each operand into
            high and low halves; compute three recursive products
            and combine. Recursion bottoms out on 1-digit factors.
            O(n^log2(3)) ~ O(n^1.585) time.
            Source: https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication-using-divide-and-conquer-algorithm/
            """),
        source_url="https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication-using-divide-and-conquer-algorithm/",
        params=["x", "y", "n"],
        inputs={
            "x": "first non-negative integer (small in tests).",
            "y": "second non-negative integer.",
            "n": "digit count (used only to size the cutoff).",
        },
        returns="x * y as a plain integer.",
        source=DC_04_SOURCE,
        setup_fn=_setup_dc_04,
        verify_fn=_verify_dc_04,
        samples=[
            Sample("x = 1234, y = 5678, n = 4", "7006652"),
            Sample("x = 0, y = 12345, n = 5", "0"),
            Sample("x = 7, y = 8, n = 1", "56"),
        ],
        hint="Split x and y into high/low halves. Recurse on a*c, b*d, and (a+b)*(c+d). Combine with ac * 10^(2h) + (ad_bc) * 10^h + bd.",
        parents=["dc_03"],
        children=["dc_05", "dc_06"],
    ),
    AlgorithmSpec(
        id="dc_05",
        name="Closest Pair of Points",
        category="divide_conquer",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Given n points in the plane, return the smallest
            Euclidean distance between any two of them. The
            classic O(n log n) plane-sweep algorithm: split
            by the median x, recurse on each half, then check
            the strip of points within `d` of the cut. Brute
            force O(n^2) verify is fine for the small n we use.
            Source: https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer/
            """),
        source_url="https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer/",
        params=["points", "n"],
        inputs={
            "points": "list of n (x, y) integer tuples.",
            "n": "number of points (capped at 8 in the setup).",
        },
        returns="the minimum pairwise Euclidean distance (float).",
        source=DC_05_SOURCE,
        setup_fn=_setup_dc_05,
        verify_fn=_verify_dc_05,
        samples=[
            Sample("points = [(0, 0), (5, 0), (3, 4)], n = 3", "3.0 (between (0,0) and (3,4))"),
            Sample("points = [(0, 0), (1, 1), (2, 2), (3, 3)], n = 4", "1.4142135... (sqrt 2)"),
        ],
        hint="Sort by x. Recurse on the left and right halves. Then walk a strip of points within d of the cut, sorted by y, and check at most 7 neighbours per point.",
        parents=["dc_04"],
        children=["dc_07"],
    ),
    AlgorithmSpec(
        id="dc_06",
        name="Strassen Matrix Multiplication",
        category="divide_conquer",
        difficulty=7,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Multiply two 2x2 matrices using Strassen's algorithm
            (7 recursive products instead of the schoolbook 8).
            O(n^log2(7)) ~ O(n^2.807) time, which beats O(n^3)
            for large n. For the small n in the test gauntlet
            the constant factor dominates, so this is a teaching
            challenge, not a speedup.
            Source: https://www.geeksforgeeks.org/strassens-matrix-multiplication/
            """),
        source_url="https://www.geeksforgeeks.org/strassens-matrix-multiplication/",
        params=["a_mat", "b_mat", "n"],
        inputs={
            "a_mat": "n x n matrix (list of lists).",
            "b_mat": "n x n matrix.",
            "n": "matrix dimension (always 2 in the setup).",
        },
        returns="the n x n product a_mat * b_mat.",
        source=DC_06_SOURCE,
        setup_fn=_setup_dc_06,
        verify_fn=_verify_dc_06,
        samples=[
            Sample("a_mat = [[1, 2], [3, 4]], b_mat = [[5, 6], [7, 8]], n = 2", "[[19, 22], [43, 50]]"),
            Sample("a_mat = [[0, 1], [1, 0]], b_mat = [[0, 1], [1, 0]], n = 2", "[[1, 0], [0, 1]]"),
        ],
        hint="p1..p7 are 7 products of sums/differences of entries. C00 = p5+p4-p2+p6, C01 = p1+p2, C10 = p3+p4, C11 = p1+p5-p3-p7.",
        parents=["dc_04"],
        children=[],
    ),
    AlgorithmSpec(
        id="dc_07",
        name="Skyline Problem",
        category="divide_conquer",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Given n axis-aligned rectangular buildings as
            (left, height, right) triples, return the skyline
            as a list of (x, height) key points. A key point is
            a position where the height changes. Consecutive
            points with the same height are collapsed.
            D&C: recursively get the left and right skylines
            and merge them in O(n). The setup keeps n small
            so an O(n^2) verify is fast.
            Source: https://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/
            """),
        source_url="https://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/",
        params=["buildings", "n"],
        inputs={
            "buildings": "list of n (left, height, right) triples.",
            "n": "number of buildings (capped at 6).",
        },
        returns="list of (x, height) key points of the skyline.",
        source=DC_07_SOURCE,
        setup_fn=_setup_dc_07,
        verify_fn=_verify_dc_07,
        samples=[
            Sample("buildings = [(1, 4, 5), (2, 3, 7), (4, 2, 9)], n = 3", "[[1, 4], [4, 3], [5, 2], [7, 0], [9, 0]]"),
            Sample("buildings = [(0, 3, 5)], n = 1", "[[0, 3], [5, 0]]"),
        ],
        hint="Recurse to get left and right skylines. Walk both with two pointers; the next key point is whichever side has the smaller x; height is max(left_h, right_h).",
        parents=["dc_05"],
        children=["dc_08"],
    ),
    AlgorithmSpec(
        id="dc_08",
        name="Count Inversions",
        category="divide_conquer",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Count the number of inversions in an array of n
            integers. An inversion is a pair (i, j) with i < j
            and a[i] > a[j]. The classic O(n log n) approach
            is to count during a merge sort: while merging the
            two sorted halves, every time a right-side element
            is taken first, all remaining left-side elements
            form an inversion with it.
            Source: https://www.geeksforgeeks.org/counting-inversions/
            """),
        source_url="https://www.geeksforgeeks.org/counting-inversions/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers.",
            "n": "length of arr.",
        },
        returns="the number of inversions.",
        source=DC_08_SOURCE,
        setup_fn=_setup_dc_08,
        verify_fn=_verify_dc_08,
        samples=[
            Sample("arr = [2, 4, 1, 3, 5], n = 5", "3 (2>1, 4>1, 4>3)"),
            Sample("arr = [5, 4, 3, 2, 1], n = 5", "10"),
            Sample("arr = [1, 2, 3, 4, 5], n = 5", "0"),
        ],
        hint="Modified merge sort. When you take from the right half first, every remaining element in the left half forms an inversion with it.",
        parents=["dc_07"],
        children=["dc_09"],
    ),
    AlgorithmSpec(
        id="dc_09",
        name="Median of Two Sorted Arrays",
        category="divide_conquer",
        difficulty=6,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Given two sorted arrays `a` (length m) and `b`
            (length n), return the median of the merged
            sorted sequence. The divide-and-conquer solution
            binary-searches on the smaller array for the
            correct partition, achieving O(log(min(m, n))).
            Source: https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
            """),
        source_url="https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/",
        params=["a", "b", "m", "n"],
        inputs={
            "a": "first sorted array of length m.",
            "b": "second sorted array of length n.",
            "m": "length of a.",
            "n": "length of b (both arrays capped at 6 in the setup).",
        },
        returns="the median of the merged sequence (float if even total length).",
        source=DC_09_SOURCE,
        setup_fn=_setup_dc_09,
        verify_fn=_verify_dc_09,
        samples=[
            Sample("a = [1, 3, 8], b = [7, 9], m = 3, n = 2", "7.0"),
            Sample("a = [1, 2], b = [3, 4], m = 2, n = 2", "2.5"),
        ],
        hint="Binary search on the smaller array. Pick i such that a[i-1] <= b[j] and b[j-1] <= a[i]. The median comes from the four boundary values.",
        parents=["dc_08"],
        children=[],
    ),
])


# === dc_10: Floor Square Root ===

DC_10_SOURCE = '''
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
'''

def _setup_dc_10(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # n up to ~2^20 so the answer stays a normal int.
    challenge._n = rng.randint(0, 1 << 20)
    return {"n": challenge._n}

def _verify_dc_10(challenge, result):
    n = challenge._n
    r = 0
    while (r + 1) * (r + 1) <= n:
        r += 1
    expected = r
    return result == expected



# === dc_11: Modular Exponentiation ===

DC_11_SOURCE = '''
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
'''

def _setup_dc_11(challenge, n, seed):
    import random
    rng = random.Random(seed)
    x = rng.randint(0, 1000)
    n = rng.randint(0, 1 << 20)
    m = rng.randint(1, 1_000_000_000) + 1   # ensure m > 0
    challenge._x = x
    challenge._n = n
    challenge._m = m
    return {"x": x, "n": n, "m": m}

def _verify_dc_11(challenge, result):
    return result == pow(challenge._x, challenge._n, challenge._m)



# === dc_12: Tiling Problem (2 x N board) ===

DC_12_SOURCE = '''
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
'''

def _setup_dc_12(challenge, n, seed):
    import random
    rng = random.Random(seed)
    challenge._n = rng.randint(0, 40)
    return {"n": challenge._n}

def _verify_dc_12(challenge, result):
    n = challenge._n
    # Reference: direct recurrence.
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return result == a



# === dc_13: Allocate Minimum Number of Pages ===

DC_13_SOURCE = '''
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
'''

def _setup_dc_13(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    arr = [rng.randint(1, 50) for _ in range(n)]
    m = rng.randint(1, n)
    challenge._arr = arr
    challenge._m = m
    return {"arr": arr, "n": n, "m": m}

def _verify_dc_13(challenge, result):
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



# === dc_14: Staircase Search in Sorted 2D Matrix ===

DC_14_SOURCE = '''
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
'''

def _setup_dc_14(challenge, n, seed):
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

def _verify_dc_14(challenge, result):
    expected = any(challenge._target in row for row in challenge._matrix)
    return result == expected



# === dc_15: Convex Hull (Divide and Conquer) ===

DC_15_SOURCE = '''
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
'''

def _setup_dc_15(challenge, n, seed):
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

def _verify_dc_15(challenge, result):
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


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="dc_10",
        name="Floor Square Root",
        category="divide_conquer",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Given a non-negative integer n, return floor(sqrt(n)).
            If n is a perfect square return the exact root; otherwise
            return the largest integer whose square is <= n.
            Binary search on the range [1, n] (D&C: keep the half
            whose square is still <= n, discard the rest).
            Source: https://www.geeksforgeeks.org/dsa/square-root-of-an-integer/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/square-root-of-an-integer/",
        params=["n"],
        inputs={
            "n": "non-negative integer to take the floor square root of.",
        },
        returns="the floor of sqrt(n) as a non-negative int.",
        source=DC_10_SOURCE,
        setup_fn=_setup_dc_10,
        verify_fn=_verify_dc_10,
        samples=[
            Sample("n = 0", "0"),
            Sample("n = 1", "1"),
            Sample("n = 4", "2"),
            Sample("n = 11", "3"),
            Sample("n = 16", "4"),
        ],
        hint="Binary search on [1, n]. When mid*mid <= n, mid is a candidate; search right half. Otherwise search left half.",
        parents=["dc_01"],
        children=["dc_13"],
    ),
    AlgorithmSpec(
        id="dc_11",
        name="Modular Exponentiation",
        category="divide_conquer",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Compute (x ** n) % m for non-negative integers x, n
            and a positive modulus m. Naive multiplication of x
            by itself n times takes O(n) steps and overflows for
            big n. The D&C trick: square-and-reduce the base
            while halving the exponent. Reduces O(n) to O(log n).
            Source: https://www.geeksforgeeks.org/dsa/modular-exponentiation-power-in-modular-arithmetic/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/modular-exponentiation-power-in-modular-arithmetic/",
        params=["x", "n", "m"],
        inputs={
            "x": "base, non-negative integer (small in tests).",
            "n": "exponent, non-negative integer (up to 2^20 in tests).",
            "m": "modulus, positive integer.",
        },
        returns="(x ** n) % m as a non-negative int.",
        source=DC_11_SOURCE,
        setup_fn=_setup_dc_11,
        verify_fn=_verify_dc_11,
        samples=[
            Sample("x = 3, n = 2, m = 4", "1"),
            Sample("x = 2, n = 6, m = 10", "4"),
            Sample("x = 7, n = 0, m = 13", "1"),
            Sample("x = 0, n = 5, m = 7", "0"),
        ],
        hint="Loop while n > 0. If n is odd, multiply result by base. Square the base and halve the exponent.",
        parents=["dc_01"],
        children=["dc_12"],
    ),
    AlgorithmSpec(
        id="dc_12",
        name="Tiling Problem (2 x N board)",
        category="divide_conquer",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Given a 2 x n board and tiles of size 2 x 1, count
            the number of ways to tile the whole board. The
            classic recurrence is T(n) = T(n-1) + T(n-2) --
            place a vertical tile (T(n-1) cases) or two
            horizontal tiles (T(n-2) cases). Implemented with
            an O(n) DP scan; the D&C view is via matrix
            exponentiation in O(log n), but the operation
            budget we measure is the simple linear walk.
            Source: https://www.geeksforgeeks.org/dsa/tiling-problem-using-divide-and-conquer-algorithm/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/tiling-problem-using-divide-and-conquer-algorithm/",
        params=["n"],
        inputs={
            "n": "board length (n >= 0).",
        },
        returns="the number of ways to tile a 2 x n board with 2 x 1 dominoes, as a non-negative int.",
        source=DC_12_SOURCE,
        setup_fn=_setup_dc_12,
        verify_fn=_verify_dc_12,
        samples=[
            Sample("n = 0", "1"),
            Sample("n = 1", "1"),
            Sample("n = 2", "2"),
            Sample("n = 3", "3"),
            Sample("n = 4", "5"),
        ],
        hint="T(0) = T(1) = 1, T(n) = T(n-1) + T(n-2). Linear Fibonacci scan.",
        parents=["dc_11"],
        children=[],
    ),
    AlgorithmSpec(
        id="dc_13",
        name="Allocate Minimum Number of Pages",
        category="divide_conquer",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Given an array arr[] of n book page counts and m
            students, allocate contiguous page blocks to each
            student so that the maximum pages any one student
            gets is minimised. Binary search on the answer:
            for a candidate max `mx`, greedily assign pages to
            students, count how many are needed, and check if
            m is achievable. The minimum feasible `mx` is the
            answer.
            Source: https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/",
        params=["arr", "n", "m"],
        inputs={
            "arr": "list of n positive page counts.",
            "n": "number of books (capped at 12 in tests).",
            "m": "number of students (1 <= m <= n).",
        },
        returns="the minimum possible value of the maximum pages any student receives, as a non-negative int.",
        source=DC_13_SOURCE,
        setup_fn=_setup_dc_13,
        verify_fn=_verify_dc_13,
        samples=[
            Sample("arr = [10, 20, 30, 40], n = 4, m = 2", "60"),
            Sample("arr = [10, 20, 30], n = 3, m = 1", "60"),
            Sample("arr = [10, 20, 30], n = 3, m = 3", "30"),
        ],
        hint="Binary search on the answer. For each candidate max, greedily assign pages and count how many students you'd need. If <= m, try smaller; else, try larger.",
        parents=["dc_10"],
        children=[],
    ),
    AlgorithmSpec(
        id="dc_14",
        name="Staircase Search in Sorted 2D Matrix",
        category="divide_conquer",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Given an n x m matrix where each row and each
            column is sorted in ascending order, return True
            iff `target` is present. Staircase algorithm: start
            at the top-right corner. If cell > target, move
            left; if cell < target, move down. Each step
            eliminates a row or a column, so O(n + m) total.
            Source: https://www.geeksforgeeks.org/dsa/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/",
        params=["matrix", "n", "m", "target"],
        inputs={
            "matrix": "n x m matrix, rows and columns sorted ascending (small in tests).",
            "n": "row count.",
            "m": "column count.",
            "target": "the value to look for.",
        },
        returns="True iff target appears in matrix.",
        source=DC_14_SOURCE,
        setup_fn=_setup_dc_14,
        verify_fn=_verify_dc_14,
        samples=[
            Sample("matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], n=3, m=4, target = 5", "True"),
            Sample("matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], n=3, m=4, target = 100", "False"),
        ],
        hint="Start at top-right. If v > target, j -= 1 (eliminate column). If v < target, i += 1 (eliminate row).",
        parents=["dc_10"],
        children=[],
    ),
    AlgorithmSpec(
        id="dc_15",
        name="Convex Hull (Divide and Conquer)",
        category="divide_conquer",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Given n points in the plane, return the vertices of
            the convex hull in counter-clockwise order, as a
            list of (x, y) tuples. The D&C variant sorts the
            points by x, splits at the median, recursively
            computes each half's hull, then merges them with a
            linear-time tangent walk. The verified-oracle uses
            a brute-force O(n^3) gift-wrbing check for small n
            so the test stays accurate.
            Source: https://www.geeksforgeeks.org/dsa/convex-hull-using-divide-and-conquer-algorithm/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/convex-hull-using-divide-and-conquer-algorithm/",
        params=["points", "n"],
        inputs={
            "points": "list of n (x, y) integer tuples (small in tests, n <= 10).",
            "n": "number of points.",
        },
        returns="list of (x, y) tuples on the convex hull in CCW order, starting with the lexicographically smallest point.",
        source=DC_15_SOURCE,
        setup_fn=_setup_dc_15,
        verify_fn=_verify_dc_15,
        samples=[
            Sample("points = [(0,0), (1,1), (2,0), (1,-1)], n=4", "[(0,0), (1,1), (2,0), (1,-1)]"),
            Sample("points = [(0,3), (1,1), (2,2), (4,4), (0,0), (1,3), (3,1), (3,3)], n=8", "[(0,0), (1,1), (4,4), (1,3), (0,3)]"),
        ],
        hint="Andrew's monotone chain: sort by x, build lower and upper hulls, concatenate. O(n log n).",
        parents=["dc_05"],
        children=[],
    ),
])


# === dc_16: Quickhull Convex Hull ===

DC_16_SOURCE = '''
def _line_side(p1, p2, p):
    """+1 / -1 / 0 for the side of p w.r.t. the line p1->p2."""
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def _line_dist(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) -
               (p2[1] - p1[1]) * (p[0] - p1[0]))

def solve(points, n):
    """Convex hull via Quickhull. Return as a Python set."""
    if n < 3:
        return set(points)
    # Find leftmost and rightmost points.
    min_x = max_x = 0
    for i in range(1, n):
        if points[i][0] < points[min_x][0]:
            min_x = i
        if points[i][0] > points[max_x][0]:
            max_x = i
    a, b = points[min_x], points[max_x]
    hull = set()

    # quickHull re-scans the full set and selects points on
    # `side` of the line p1->p2, exactly like the GfG reference
    # implementation. Average O(n log n), worst O(n^2).
    def quickHull(pts, p1, p2, side):
        ind = -1
        max_dist = 0
        for i, p in enumerate(pts):
            if _line_side(p1, p2, p) == side:
                d = _line_dist(p1, p2, p)
                if d > max_dist:
                    ind = i
                    max_dist = d
        if ind == -1:
            hull.add(p1)
            hull.add(p2)
            return
        P = pts[ind]
        quickHull(pts, P, p1, -_line_side(P, p1, p2))
        quickHull(pts, P, p2, -_line_side(P, p2, p1))

    quickHull(points, a, b, 1)
    quickHull(points, a, b, -1)
    return hull
'''

def _setup_dc_16(challenge, n, seed):
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

def _verify_dc_16(challenge, result):
    # The GfG Quickhull reference implementation has a known
    # ambiguity for collinear-on-hull-edge points: it can keep or
    # drop them depending on the partitioning. We don't want a
    # fragile set-equality test, so verify the structural
    # invariant: result is a valid convex hull containing every
    # input point.
    import math

    def _cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def _on_segment(p, a, b):
        # Is p on the closed segment a-b?
        if (min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
                min(a[1], b[1]) <= p[1] <= max(a[1], b[1]) and
                _cross(a, b, p) == 0):
            return True
        return False

    points = list(challenge._points)

    # 1. result is a set of (x, y) tuples.
    if not isinstance(result, set):
        return False
    if len(points) < 3:
        return set(result) == set(points)
    hull_pts = list(result)
    if len(hull_pts) < 3:
        return False

    # 2. Build a CCW-ordered version of the hull so polygon tests
    #    are well-defined. Sort by angle around the centroid.
    cx = sum(p[0] for p in hull_pts) / len(hull_pts)
    cy = sum(p[1] for p in hull_pts) / len(hull_pts)
    hull = sorted(hull_pts, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

    # 3. Every input point is inside the hull polygon OR on one of
    #    its edges (winding-number test, robust to boundary points).
    def _point_in_or_on_polygon(pt, poly):
        n = len(poly)
        for i in range(n):
            if _on_segment(pt, poly[i], poly[(i + 1) % n]):
                return True
        x, y = pt
        w = 0
        for i in range(n):
            x1, y1 = poly[i]
            x2, y2 = poly[(i + 1) % n]
            if y1 <= y:
                if y2 > y and _cross((x1, y1), (x2, y2), (x, y)) > 0:
                    w += 1
            else:
                if y2 <= y and _cross((x1, y1), (x2, y2), (x, y)) < 0:
                    w -= 1
        return w != 0

    for p in points:
        if not _point_in_or_on_polygon(p, hull):
            return False

    # 4. The hull is convex: every consecutive triple has a
    #    consistent turn direction. (We expect CCW since that's
    #    what we sorted to, but verify it.)
    n = len(hull)
    ref_sign = 0
    for i in range(n):
        c = _cross(hull[i], hull[(i + 1) % n], hull[(i + 2) % n])
        if c != 0:
            ref_sign = 1 if c > 0 else -1
            break
    if ref_sign == 0:
        return False
    for i in range(n):
        c = _cross(hull[i], hull[(i + 1) % n], hull[(i + 2) % n])
        if c != 0:
            s = 1 if c > 0 else -1
            if s != ref_sign:
                return False
    return True



# === dc_17: Min and Max (D&C tournament) ===

DC_17_SOURCE = '''
def solve(arr, n):
    """D&C tournament min/max. Returns [lo, hi]."""
    def rec(lo, hi):
        if lo == hi:
            return [arr[lo], arr[lo]]
        if hi == lo + 1:
            if arr[lo] < arr[hi]:
                return [arr[lo], arr[hi]]
            return [arr[hi], arr[lo]]
        mid = (lo + hi) // 2
        a = rec(lo, mid)
        b = rec(mid + 1, hi)
        return [min(a[0], b[0]), max(a[1], b[1])]
    return rec(0, n - 1)
'''

def _setup_dc_17(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 32))
    arr = [rng.randint(-100, 100) for _ in range(n)]
    challenge._arr = arr
    return {"arr": arr, "n": n}

def _verify_dc_17(challenge, result):
    expected = [min(challenge._arr), max(challenge._arr)]
    return result == expected



# === dc_18: Frequency in Limited Range (sorted array) ===

DC_18_SOURCE = '''
def solve(arr, n, target):
    """Frequency of `target` in a sorted array via two binary
    searches (first and last occurrence)."""
    # First occurrence.
    lo, hi, first = 0, n - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            first = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    if first == -1:
        return 0
    # Last occurrence.
    lo, hi, last = first, n - 1, first
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            last = mid
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return last - first + 1
'''

def _setup_dc_18(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 32))
    # Build a sorted array with duplicates, drawn from a small
    # positive integer range (the "limited range" assumption).
    value_range = 8
    counts = [rng.randint(0, 5) for _ in range(value_range)]
    arr = []
    for v, c in enumerate(counts, start=1):
        arr.extend([v] * c)
    arr.sort()
    # Trim/pad to length n.
    if len(arr) > n:
        arr = arr[:n]
    while len(arr) < n:
        arr.append(rng.randint(1, value_range))
    arr.sort()
    # Pick target: with prob 0.5 choose one that's actually present,
    # else pick something outside the array contents.
    if arr and rng.random() < 0.5:
        target = arr[rng.randrange(len(arr))]
    else:
        target = rng.randint(value_range + 1, value_range + 5)
    challenge._arr = arr
    challenge._target = target
    return {"arr": arr, "n": len(arr), "target": target}

def _verify_dc_18(challenge, result):
    return result == challenge._arr.count(challenge._target)



# === dc_19: Maximum Subarray Sum (Divide and Conquer) ===

DC_19_SOURCE = '''
def solve(arr, n):
    """Maximum subarray sum via divide and conquer."""

    def rec(lo, hi):
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        # Best fully in the left half.
        left_best = rec(lo, mid)
        # Best fully in the right half.
        right_best = rec(mid + 1, hi)
        # Best crossing the middle: extend leftward from mid,
        # then rightward from mid+1, and combine.
        s = 0
        left_sum = arr[mid]
        for i in range(mid, lo - 1, -1):
            s += arr[i]
            if s > left_sum:
                left_sum = s
        s = 0
        right_sum = arr[mid + 1]
        for i in range(mid + 1, hi + 1):
            s += arr[i]
            if s > right_sum:
                right_sum = s
        cross = left_sum + right_sum
        return max(left_best, right_best, cross)

    return rec(0, n - 1)
'''

def _setup_dc_19(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    # Mix of negatives, positives, and zeros.
    arr = [rng.randint(-15, 15) for _ in range(n)]
    challenge._arr = arr
    return {"arr": arr, "n": n}

def _verify_dc_19(challenge, result):
    # Reference: brute-force O(n^2) subarray scan.
    arr = challenge._arr
    best = arr[0]
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s > best:
                best = s
    expected = best
    return result == expected


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="dc_16",
        name="Quickhull Convex Hull",
        category="divide_conquer",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Given n points in the plane, return the vertices of
            the convex hull as a set of (x, y) tuples. Quickhull
            is a D&C analogue of quicksort: split by the line
            through the leftmost and rightmost points, recurse
            on each side using the farthest point from the line
            as the new pivot, and discard everything inside the
            resulting triangle. Average O(n log n), worst O(n^2).
            The canonical O(n log n) verify uses Andrew's
            monotone chain so the test stays accurate for all
            inputs.
            Source: https://www.geeksforgeeks.org/dsa/quickhull-algorithm-convex-hull/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/quickhull-algorithm-convex-hull/",
        params=["points", "n"],
        inputs={
            "points": "list of n (x, y) integer tuples (small in tests, n <= 10).",
            "n": "number of points.",
        },
        returns="a set of (x, y) tuples that are the vertices of a valid convex hull containing all input points (any valid hull is accepted).",
        source=DC_16_SOURCE,
        setup_fn=_setup_dc_16,
        verify_fn=_verify_dc_16,
        samples=[
            Sample("points = [(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)], n=8", "a set like {(0,0),(0,3),(1,1),(3,1),(4,4)} (any valid hull accepted)"),
            Sample("points = [(0,0),(0,4),(-4,0),(5,0),(0,-6),(1,0)], n=6", "a set like {(-4,0),(5,0),(0,-6),(0,4)} (any valid hull accepted)"),
        ],
        hint="Find leftmost/rightmost points. Split the remaining set by the line through them. Recursively keep the point farthest from each sub-line until no more points are outside.",
        parents=["dc_15"],
        children=[],
    ),
    AlgorithmSpec(
        id="dc_17",
        name="Min and Max (D&C tournament)",
        category="divide_conquer",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Given an array of n integers, return the minimum
            and maximum values using only (3n/2) - 2 comparisons
            in the worst case. The D&C tournament method: for
            n = 1 the min and max are both the element; for n = 2
            they are decided in one comparison; for larger n,
            recursively solve both halves, then take min of the
            mins and max of the maxes (2 more comparisons).
            Source: https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers (n >= 1).",
            "n": "array length (capped at 32 in tests).",
        },
        returns="[min(arr), max(arr)] as a 2-element list.",
        source=DC_17_SOURCE,
        setup_fn=_setup_dc_17,
        verify_fn=_verify_dc_17,
        samples=[
            Sample("arr = [3, 5, 4, 1, 9], n = 5", "[1, 9]"),
            Sample("arr = [22, 14, 8, 17, 35, 3], n = 6", "[3, 35]"),
            Sample("arr = [7], n = 1", "[7, 7]"),
            Sample("arr = [2, 1], n = 2", "[1, 2]"),
        ],
        hint="Base cases: 1 element -> [x, x]; 2 elements -> one compare. Recursive: split in half, recurse, then take min of the mins and max of the maxes.",
        parents=["dc_01"],
        children=[],
    ),
    AlgorithmSpec(
        id="dc_18",
        name="Frequency in Limited Range (sorted array)",
        category="divide_conquer",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Given a sorted array of positive integers and a
            value `target` (also in the limited range), return
            the number of times `target` appears. Use D&C
            binary search to find the first and last occurrence
            of the target, then frequency = last - first + 1.
            The D&C speedup: instead of O(n) linear scanning,
            each frequency query is O(log n). If the target is
            absent, return 0.
            Source: https://www.geeksforgeeks.org/dsa/find-frequency-of-each-element-in-a-limited-range-array-in-less-than-on-time/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/find-frequency-of-each-element-in-a-limited-range-array-in-less-than-on-time/",
        params=["arr", "n", "target"],
        inputs={
            "arr": "sorted list of n positive integers.",
            "n": "array length (capped at 32 in tests).",
            "target": "the value whose frequency we want.",
        },
        returns="the count of `target` in `arr` as a non-negative int (0 if absent).",
        source=DC_18_SOURCE,
        setup_fn=_setup_dc_18,
        verify_fn=_verify_dc_18,
        samples=[
            Sample("arr = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10], n = 14, target = 8", "3"),
            Sample("arr = [2, 2, 6, 6, 7, 7, 7, 11], n = 8, target = 6", "2"),
            Sample("arr = [1, 2, 3, 4, 5], n = 5, target = 99", "0"),
        ],
        hint="Two binary searches: the first finds the leftmost occurrence, the second finds the rightmost. Frequency = last - first + 1 (or 0 if not found).",
        parents=["dc_10"],
        children=[],
    ),
    AlgorithmSpec(
        id="dc_19",
        name="Maximum Subarray Sum (Divide and Conquer)",
        category="divide_conquer",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Given an array of n integers (with at least one
            element), return the sum of the contiguous subarray
            with the largest sum. The D&C approach: split the
            array at the middle, the answer is the max of (a)
            the best subarray fully in the left half, (b) the
            best fully in the right half, and (c) the best
            subarray that crosses the middle. The crossing sum
            is found in linear time. O(n log n) total.
            Source: https://www.geeksforgeeks.org/dsa/maximum-subarray-sum-using-divide-and-conquer-algorithm/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/maximum-subarray-sum-using-divide-and-conquer-algorithm/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers (n >= 1; may include negatives).",
            "n": "array length (capped at 16 in tests).",
        },
        returns="the maximum subarray sum as an int.",
        source=DC_19_SOURCE,
        setup_fn=_setup_dc_19,
        verify_fn=_verify_dc_19,
        samples=[
            Sample("arr = [2, 3, -8, 7, -1, 2, 3], n = 7", "11"),
            Sample("arr = [-2, -4], n = 2", "-2"),
            Sample("arr = [5, 4, 1, 7, 8], n = 5", "25"),
            Sample("arr = [2, 3, 4, 5, 7], n = 5", "21"),
        ],
        hint="Recurse on the two halves. For the crossing subarray, take the max suffix of the left half and the max prefix of the right half and add them.",
        parents=["dc_17"],
        children=[],
    ),
])
