"""Spec generator input — 6 divide-and-conquer specs for Session 1.

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module divide_conquer \\
        --input batch_dc_session1.py
"""


SPECS_TO_ADD = [
    {
        "id": "dc_04",
        "name": "Karatsuba Multiplication",
        "category": "divide_conquer",
        "difficulty": 6,
        "complexity": "O_N_LOG_N",
        "description": (
            "Multiply two non-negative integers using Karatsuba's\n"
            "divide-and-conquer algorithm. Split each operand into\n"
            "high and low halves; compute three recursive products\n"
            "and combine. Recursion bottoms out on 1-digit factors.\n"
            "O(n^log2(3)) ~ O(n^1.585) time.\n"
            "Source: https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication-using-divide-and-conquer-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication-using-divide-and-conquer-algorithm/",
        "params": ["x", "y", "n"],
        "inputs": {
            "x": "first non-negative integer (small in tests).",
            "y": "second non-negative integer.",
            "n": "digit count (used only to size the cutoff).",
        },
        "returns": "x * y as a plain integer.",
        "solve": '''
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
''',
        "setup": '''
rng = random.Random(seed)
x = rng.randint(0, 9999)
y = rng.randint(0, 9999)
challenge._x = x
challenge._y = y
return {"x": x, "y": y, "n": max(len(str(x)), len(str(y)))}
''',
        "verify": '''
return isinstance(result, int) and result == challenge._x * challenge._y
''',
        "samples": [
            ("x = 1234, y = 5678, n = 4", "7006652"),
            ("x = 0, y = 12345, n = 5", "0"),
            ("x = 7, y = 8, n = 1", "56"),
        ],
        "hint": "Split x and y into high/low halves. Recurse on a*c, b*d, and (a+b)*(c+d). Combine with ac * 10^(2h) + (ad_bc) * 10^h + bd.",
        "parents": ["dc_03"],
        "children": ["dc_05", "dc_06"],
    },
    {
        "id": "dc_05",
        "name": "Closest Pair of Points",
        "category": "divide_conquer",
        "difficulty": 6,
        "complexity": "O_N2",
        "description": (
            "Given n points in the plane, return the smallest\n"
            "Euclidean distance between any two of them. The\n"
            "classic O(n log n) plane-sweep algorithm: split\n"
            "by the median x, recurse on each half, then check\n"
            "the strip of points within `d` of the cut. Brute\n"
            "force O(n^2) verify is fine for the small n we use.\n"
            "Source: https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer/"
        ),
        "source_url": "https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer/",
        "params": ["points", "n"],
        "inputs": {
            "points": "list of n (x, y) integer tuples.",
            "n": "number of points (capped at 8 in the setup).",
        },
        "returns": "the minimum pairwise Euclidean distance (float).",
        "solve": '''
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
''',
        "setup": '''
rng = random.Random(seed)
n_pts = max(2, min(n, 8))
points = [(rng.randint(-10, 10), rng.randint(-10, 10)) for _ in range(n_pts)]
challenge._points = points
return {"points": points, "n": n_pts}
''',
        "verify": '''
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
''',
        "samples": [
            ("points = [(0, 0), (5, 0), (3, 4)], n = 3", "3.0 (between (0,0) and (3,4))"),
            ("points = [(0, 0), (1, 1), (2, 2), (3, 3)], n = 4", "1.4142135... (sqrt 2)"),
        ],
        "hint": "Sort by x. Recurse on the left and right halves. Then walk a strip of points within d of the cut, sorted by y, and check at most 7 neighbours per point.",
        "parents": ["dc_04"],
        "children": ["dc_07"],
    },
    {
        "id": "dc_06",
        "name": "Strassen Matrix Multiplication",
        "category": "divide_conquer",
        "difficulty": 7,
        "complexity": "O_N_LOG_N",
        "description": (
            "Multiply two 2x2 matrices using Strassen's algorithm\n"
            "(7 recursive products instead of the schoolbook 8).\n"
            "O(n^log2(7)) ~ O(n^2.807) time, which beats O(n^3)\n"
            "for large n. For the small n in the test gauntlet\n"
            "the constant factor dominates, so this is a teaching\n"
            "challenge, not a speedup.\n"
            "Source: https://www.geeksforgeeks.org/strassens-matrix-multiplication/"
        ),
        "source_url": "https://www.geeksforgeeks.org/strassens-matrix-multiplication/",
        "params": ["A", "B", "n"],
        "inputs": {
            "A": "n x n matrix (list of lists).",
            "B": "n x n matrix.",
            "n": "matrix dimension (always 2 in the setup).",
        },
        "returns": "the n x n product A * B.",
        "solve": '''
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
''',
        "setup": '''
rng = random.Random(seed)
n_dim = 2
A = [[rng.randint(-5, 5) for _ in range(n_dim)] for _ in range(n_dim)]
B = [[rng.randint(-5, 5) for _ in range(n_dim)] for _ in range(n_dim)]
challenge._A = A
challenge._B = B
return {"A": A, "B": B, "n": n_dim}
''',
        "verify": '''
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
''',
        "samples": [
            ("A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]], n = 2", "[[19, 22], [43, 50]]"),
            ("A = [[0, 1], [1, 0]], B = [[0, 1], [1, 0]], n = 2", "[[1, 0], [0, 1]]"),
        ],
        "hint": "p1..p7 are 7 products of sums/differences of entries. C00 = p5+p4-p2+p6, C01 = p1+p2, C10 = p3+p4, C11 = p1+p5-p3-p7.",
        "parents": ["dc_04"],
        "children": [],
    },
    {
        "id": "dc_07",
        "name": "Skyline Problem",
        "category": "divide_conquer",
        "difficulty": 5,
        "complexity": "O_N2",
        "description": (
            "Given n axis-aligned rectangular buildings as\n"
            "(left, height, right) triples, return the skyline\n"
            "as a list of (x, height) key points. A key point is\n"
            "a position where the height changes. Consecutive\n"
            "points with the same height are collapsed.\n"
            "D&C: recursively get the left and right skylines\n"
            "and merge them in O(n). The setup keeps n small\n"
            "so an O(n^2) verify is fast.\n"
            "Source: https://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/"
        ),
        "source_url": "https://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/",
        "params": ["buildings", "n"],
        "inputs": {
            "buildings": "list of n (left, height, right) triples.",
            "n": "number of buildings (capped at 6).",
        },
        "returns": "list of (x, height) key points of the skyline.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("buildings = [(1, 4, 5), (2, 3, 7), (4, 2, 9)], n = 3", "[[1, 4], [4, 3], [5, 2], [7, 0], [9, 0]]"),
            ("buildings = [(0, 3, 5)], n = 1", "[[0, 3], [5, 0]]"),
        ],
        "hint": "Recurse to get left and right skylines. Walk both with two pointers; the next key point is whichever side has the smaller x; height is max(left_h, right_h).",
        "parents": ["dc_05"],
        "children": ["dc_08"],
    },
    {
        "id": "dc_08",
        "name": "Count Inversions",
        "category": "divide_conquer",
        "difficulty": 4,
        "complexity": "O_N_LOG_N",
        "description": (
            "Count the number of inversions in an array of n\n"
            "integers. An inversion is a pair (i, j) with i < j\n"
            "and a[i] > a[j]. The classic O(n log n) approach\n"
            "is to count during a merge sort: while merging the\n"
            "two sorted halves, every time a right-side element\n"
            "is taken first, all remaining left-side elements\n"
            "form an inversion with it.\n"
            "Source: https://www.geeksforgeeks.org/counting-inversions/"
        ),
        "source_url": "https://www.geeksforgeeks.org/counting-inversions/",
        "params": ["arr", "n"],
        "inputs": {
            "arr": "list of n integers.",
            "n": "length of arr.",
        },
        "returns": "the number of inversions.",
        "solve": '''
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
''',
        "setup": '''
rng = random.Random(seed)
n_arr = max(1, min(n, 10))
arr = [rng.randint(0, 9) for _ in range(n_arr)]
challenge._arr = arr
return {"arr": arr, "n": n_arr}
''',
        "verify": '''
arr = challenge._arr
n = len(arr)
expected = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            expected += 1
return result == expected
''',
        "samples": [
            ("arr = [2, 4, 1, 3, 5], n = 5", "3 (2>1, 4>1, 4>3)"),
            ("arr = [5, 4, 3, 2, 1], n = 5", "10"),
            ("arr = [1, 2, 3, 4, 5], n = 5", "0"),
        ],
        "hint": "Modified merge sort. When you take from the right half first, every remaining element in the left half forms an inversion with it.",
        "parents": ["dc_07"],
        "children": ["dc_09"],
    },
    {
        "id": "dc_09",
        "name": "Median of Two Sorted Arrays",
        "category": "divide_conquer",
        "difficulty": 6,
        "complexity": "O_LOG_N",
        "description": (
            "Given two sorted arrays `a` (length m) and `b`\n"
            "(length n), return the median of the merged\n"
            "sorted sequence. The divide-and-conquer solution\n"
            "binary-searches on the smaller array for the\n"
            "correct partition, achieving O(log(min(m, n))).\n"
            "Source: https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/"
        ),
        "source_url": "https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/",
        "params": ["a", "b", "m", "n"],
        "inputs": {
            "a": "first sorted array of length m.",
            "b": "second sorted array of length n.",
            "m": "length of a.",
            "n": "length of b (both arrays capped at 6 in the setup).",
        },
        "returns": "the median of the merged sequence (float if even total length).",
        "solve": '''
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
''',
        "setup": '''
rng = random.Random(seed)
m = max(1, min(n, 6))
remaining = max(1, min(n, 6))
a = sorted(rng.randint(0, 9) for _ in range(m))
b = sorted(rng.randint(0, 9) for _ in range(remaining))
challenge._a = a
challenge._b = b
return {"a": a, "b": b, "m": m, "n": remaining}
''',
        "verify": '''
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
''',
        "samples": [
            ("a = [1, 3, 8], b = [7, 9], m = 3, n = 2", "7.0"),
            ("a = [1, 2], b = [3, 4], m = 2, n = 2", "2.5"),
        ],
        "hint": "Binary search on the smaller array. Pick i such that a[i-1] <= b[j] and b[j-1] <= a[i]. The median comes from the four boundary values.",
        "parents": ["dc_08"],
        "children": [],
    },
]
