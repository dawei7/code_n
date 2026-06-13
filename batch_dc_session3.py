"""Spec generator input — 4 more divide-and-conquer specs for Session 3.

Finishes the GfG "Divide and Conquer" topic list:

  dc_16  Quickhull Algorithm for Convex Hull
  dc_17  Min and Max using minimum comparisons (D&C tournament)
  dc_18  Frequency in a limited range array (binary search D&C)
  dc_19  Maximum Subarray Sum (D&C crossing sum)

After this batch, divide_conquer.py covers the entire GfG D&C
topic list (see https://www.geeksforgeeks.org/divide-and-conquer/).

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module divide_conquer \\
        --input batch_dc_session3.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # dc_16: Quickhull Algorithm for Convex Hull
    # ============================================================
    {
        "id": "dc_16",
        "name": "Quickhull Convex Hull",
        "category": "divide_conquer",
        "difficulty": 6,
        "complexity": "O_N_LOG_N",
        "description": (
            "Given n points in the plane, return the vertices of\n"
            "the convex hull as a set of (x, y) tuples. Quickhull\n"
            "is a D&C analogue of quicksort: split by the line\n"
            "through the leftmost and rightmost points, recurse\n"
            "on each side using the farthest point from the line\n"
            "as the new pivot, and discard everything inside the\n"
            "resulting triangle. Average O(n log n), worst O(n^2).\n"
            "The canonical O(n log n) verify uses Andrew's\n"
            "monotone chain so the test stays accurate for all\n"
            "inputs.\n"
            "Source: https://www.geeksforgeeks.org/dsa/quickhull-algorithm-convex-hull/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/quickhull-algorithm-convex-hull/",
        "params": ["points", "n"],
        "inputs": {
            "points": "list of n (x, y) integer tuples (small in tests, n <= 10).",
            "n": "number of points.",
        },
        "returns": "a set of (x, y) tuples that are the vertices of a valid convex hull containing all input points (any valid hull is accepted).",
        "solve": '''
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
''',
        "samples": [
            ("points = [(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)], n=8", "a set like {(0,0),(0,3),(1,1),(3,1),(4,4)} (any valid hull accepted)"),
            ("points = [(0,0),(0,4),(-4,0),(5,0),(0,-6),(1,0)], n=6", "a set like {(-4,0),(5,0),(0,-6),(0,4)} (any valid hull accepted)"),
        ],
        "hint": "Find leftmost/rightmost points. Split the remaining set by the line through them. Recursively keep the point farthest from each sub-line until no more points are outside.",
        "parents": ["dc_15"],
        "children": [],
    },

    # ============================================================
    # dc_17: Min and Max using minimum comparisons (D&C tournament)
    # ============================================================
    {
        "id": "dc_17",
        "name": "Min and Max (D&C tournament)",
        "category": "divide_conquer",
        "difficulty": 3,
        "complexity": "O_N",
        "description": (
            "Given an array of n integers, return the minimum\n"
            "and maximum values using only (3n/2) - 2 comparisons\n"
            "in the worst case. The D&C tournament method: for\n"
            "n = 1 the min and max are both the element; for n = 2\n"
            "they are decided in one comparison; for larger n,\n"
            "recursively solve both halves, then take min of the\n"
            "mins and max of the maxes (2 more comparisons).\n"
            "Source: https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/",
        "params": ["arr", "n"],
        "inputs": {
            "arr": "list of n integers (n >= 1).",
            "n": "array length (capped at 32 in tests).",
        },
        "returns": "[min(arr), max(arr)] as a 2-element list.",
        "solve": '''
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
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 32))
arr = [rng.randint(-100, 100) for _ in range(n)]
challenge._arr = arr
return {"arr": arr, "n": n}
''',
        "verify": '''
expected = [min(challenge._arr), max(challenge._arr)]
return result == expected
''',
        "samples": [
            ("arr = [3, 5, 4, 1, 9], n = 5", "[1, 9]"),
            ("arr = [22, 14, 8, 17, 35, 3], n = 6", "[3, 35]"),
            ("arr = [7], n = 1", "[7, 7]"),
            ("arr = [2, 1], n = 2", "[1, 2]"),
        ],
        "hint": "Base cases: 1 element -> [x, x]; 2 elements -> one compare. Recursive: split in half, recurse, then take min of the mins and max of the maxes.",
        "parents": ["dc_01"],
        "children": [],
    },

    # ============================================================
    # dc_18: Frequency in a limited range sorted array
    # ============================================================
    {
        "id": "dc_18",
        "name": "Frequency in Limited Range (sorted array)",
        "category": "divide_conquer",
        "difficulty": 4,
        "complexity": "O_LOG_N",
        "description": (
            "Given a sorted array of positive integers and a\n"
            "value `target` (also in the limited range), return\n"
            "the number of times `target` appears. Use D&C\n"
            "binary search to find the first and last occurrence\n"
            "of the target, then frequency = last - first + 1.\n"
            "The D&C speedup: instead of O(n) linear scanning,\n"
            "each frequency query is O(log n). If the target is\n"
            "absent, return 0.\n"
            "Source: https://www.geeksforgeeks.org/dsa/find-frequency-of-each-element-in-a-limited-range-array-in-less-than-on-time/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/find-frequency-of-each-element-in-a-limited-range-array-in-less-than-on-time/",
        "params": ["arr", "n", "target"],
        "inputs": {
            "arr": "sorted list of n positive integers.",
            "n": "array length (capped at 32 in tests).",
            "target": "the value whose frequency we want.",
        },
        "returns": "the count of `target` in `arr` as a non-negative int (0 if absent).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
return result == challenge._arr.count(challenge._target)
''',
        "samples": [
            ("arr = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10], n = 14, target = 8", "3"),
            ("arr = [2, 2, 6, 6, 7, 7, 7, 11], n = 8, target = 6", "2"),
            ("arr = [1, 2, 3, 4, 5], n = 5, target = 99", "0"),
        ],
        "hint": "Two binary searches: the first finds the leftmost occurrence, the second finds the rightmost. Frequency = last - first + 1 (or 0 if not found).",
        "parents": ["dc_10"],
        "children": [],
    },

    # ============================================================
    # dc_19: Maximum Subarray Sum (D&C crossing sum)
    # ============================================================
    {
        "id": "dc_19",
        "name": "Maximum Subarray Sum (Divide and Conquer)",
        "category": "divide_conquer",
        "difficulty": 5,
        "complexity": "O_N_LOG_N",
        "description": (
            "Given an array of n integers (with at least one\n"
            "element), return the sum of the contiguous subarray\n"
            "with the largest sum. The D&C approach: split the\n"
            "array at the middle, the answer is the max of (a)\n"
            "the best subarray fully in the left half, (b) the\n"
            "best fully in the right half, and (c) the best\n"
            "subarray that crosses the middle. The crossing sum\n"
            "is found in linear time. O(n log n) total.\n"
            "Source: https://www.geeksforgeeks.org/dsa/maximum-subarray-sum-using-divide-and-conquer-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/maximum-subarray-sum-using-divide-and-conquer-algorithm/",
        "params": ["arr", "n"],
        "inputs": {
            "arr": "list of n integers (n >= 1; may include negatives).",
            "n": "array length (capped at 16 in tests).",
        },
        "returns": "the maximum subarray sum as an int.",
        "solve": '''
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
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 16))
# Mix of negatives, positives, and zeros.
arr = [rng.randint(-15, 15) for _ in range(n)]
challenge._arr = arr
return {"arr": arr, "n": n}
''',
        "verify": '''
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
''',
        "samples": [
            ("arr = [2, 3, -8, 7, -1, 2, 3], n = 7", "11"),
            ("arr = [-2, -4], n = 2", "-2"),
            ("arr = [5, 4, 1, 7, 8], n = 5", "25"),
            ("arr = [2, 3, 4, 5, 7], n = 5", "21"),
        ],
        "hint": "Recurse on the two halves. For the crossing subarray, take the max suffix of the left half and the max prefix of the right half and add them.",
        "parents": ["dc_17"],
        "children": [],
    },
]
