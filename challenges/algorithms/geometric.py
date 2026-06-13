"""Geometric algorithms.

Three classic problems from GFG's geometric-algorithms catalog:

  01 Closest Pair of Points           - O(n log n) divide and conquer
  02 Convex Hull (Graham Scan)       - sort by polar angle
  03 Line Segment Intersection       - check every pair

The setup keeps n small (4-16) so brute-force verification
is fast. Points are passed as a list of (x, y) tuples.
"""


from __future__ import annotations

import math
import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === geometric_01: Closest Pair of Points ===

GEO_01_SOURCE = '''\
"""Optimal solution for geometric_01: Closest Pair of Points.

Brute-force O(n^2) for the test gauntlet. Check every pair;
return the smallest distance and the pair that achieves it.
"""


def solve(points, n):
    if n < 2:
        return -1, [(0, 0), (0, 0)]
    best_d = float("inf")
    best_pair = (points[0], points[1])
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            d = dx * dx + dy * dy
            if d < best_d:
                best_d = d
                best_pair = (points[i], points[j])
    return best_d, sorted(best_pair)
'''


def _setup_closest_pair(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(2, min(n, 12))
    points = [(rng.randint(0, 30), rng.randint(0, 30)) for _ in range(n)]
    challenge._points = list(points)
    return {"points": list(points), "n": n}


def _verify_closest_pair(challenge, result: Any) -> bool:
    if not isinstance(result, tuple) or len(result) != 2:
        return False
    d, pair = result
    if not isinstance(d, (int, float)) or not isinstance(pair, list) or len(pair) != 2:
        return False
    points = challenge._points
    if sorted(pair) != sorted(pair):  # check pair is sorted
        return False
    # Brute force to verify distance.
    expected_d = float("inf")
    expected_pair = (points[0], points[1])
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist = dx * dx + dy * dy
            if dist < expected_d:
                expected_d = dist
                expected_pair = (points[i], points[j])
    return d == expected_d and sorted(pair) == sorted(expected_pair)


# === geometric_02: Convex Hull (Graham Scan) ===

GEO_02_SOURCE = '''\
"""Optimal solution for geometric_02: Convex Hull (Graham Scan).

Bottom-most, then leftmost point is the pivot. Sort the rest
by polar angle to the pivot. Walk the sorted list, pushing to
a stack; pop the stack while the top two and the new point
make a non-left turn. O(n log n).
"""


def solve(points, n):
    import math
    if n < 3:
        return sorted(points)
    # Pick the pivot: bottom-most, then left-most.
    pivot = min(points)
    def angle_key(p):
        if p == pivot:
            return (-math.inf,)
        dx = p[0] - pivot[0]
        dy = p[1] - pivot[1]
        # Sort by (atan2, distance) - use atan2 since we want
        # consistent ordering for the same angle.
        return (math.atan2(dy, dx), dx * dx + dy * dy)
    rest = [p for p in points if p != pivot]
    rest.sort(key=angle_key)
    # Build the hull with a stack.
    hull = [pivot]
    for p in rest:
        while len(hull) >= 2:
            o, a = hull[-2], hull[-1]
            cross = (a[0] - o[0]) * (p[1] - o[1]) - (a[1] - o[1]) * (p[0] - o[0])
            if cross <= 0:
                hull.pop()
            else:
                break
        hull.append(p)
    return sorted(hull)
'''


def _setup_convex_hull(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(3, min(n, 10))
    points = []
    while len(points) < n:
        p = (rng.randint(0, 20), rng.randint(0, 20))
        if p not in points:
            points.append(p)
    challenge._points = list(points)
    return {"points": list(points), "n": n}


def _verify_convex_hull(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    # Brute-force: gift wrapping O(n^2) - returns the hull in CCW order.
    points = challenge._points
    if len(points) < 3:
        return result == sorted(points)
    # Gift wrapping.
    hull = []
    # Start with the leftmost point.
    leftmost = min(points)
    cur = leftmost
    while True:
        hull.append(cur)
        candidate = None
        for p in points:
            if p == cur:
                continue
            if candidate is None:
                candidate = p
                continue
            # Check that p is to the left of (cur, candidate).
            cross = (candidate[0] - cur[0]) * (p[1] - cur[1]) - (candidate[1] - cur[1]) * (p[0] - cur[0])
            if cross < 0:
                candidate = p
        if candidate is None or candidate == leftmost:
            break
        cur = candidate
        if cur in hull:
            break
    # Compare as sorted sets (the verify doesn't care about order).
    return sorted(result) == sorted(hull)


# === geometric_03: Line Segment Intersection ===

GEO_03_SOURCE = '''\
"""Optimal solution for geometric_03: Line Segment Intersection.

Given two line segments, each as ((x1, y1), (x2, y2)). They
intersect iff the orientations of the two endpoint triples
straddle each other. Standard cross-product trick.
"""


def solve(seg1, seg2):
    def orient(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    def on_segment(a, b, c):
        return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and
                min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))
    (p1, q1) = seg1
    (p2, q2) = seg2
    o1 = orient(p1, q1, p2)
    o2 = orient(p1, q1, q2)
    o3 = orient(p2, q2, p1)
    o4 = orient(p2, q2, q1)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    if o1 == 0 and on_segment(p1, q1, p2):
        return True
    if o2 == 0 and on_segment(p1, q1, q2):
        return True
    if o3 == 0 and on_segment(p2, q2, p1):
        return True
    if o4 == 0 and on_segment(p2, q2, q1):
        return True
    return False
'''


def _setup_line_intersect(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # ~half the time, build two segments that intersect.
    if rng.random() < 0.5:
        # Crossing X.
        p1 = (0, 0)
        q1 = (10, 10)
        p2 = (0, 10)
        q2 = (10, 0)
    else:
        # Parallel or non-crossing.
        p1 = (0, 0)
        q1 = (10, 5)
        p2 = (0, 10)
        q2 = (10, 15)
    challenge._seg1 = (p1, q1)
    challenge._seg2 = (p2, q2)
    return {"seg1": [p1, q1], "seg2": [p2, q2]}


def _verify_line_intersect(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    seg1 = challenge._seg1
    seg2 = challenge._seg2
    # Re-run the canonical algorithm (inlined) for verification.
    def orient(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    def on_segment(a, b, c):
        return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and
                min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))
    (p1, q1) = seg1
    (p2, q2) = seg2
    o1 = orient(p1, q1, p2)
    o2 = orient(p1, q1, q2)
    o3 = orient(p2, q2, p1)
    o4 = orient(p2, q2, q1)
    expected = False
    if o1 * o2 < 0 and o3 * o4 < 0:
        expected = True
    elif o1 == 0 and on_segment(p1, q1, p2):
        expected = True
    elif o2 == 0 and on_segment(p1, q1, q2):
        expected = True
    elif o3 == 0 and on_segment(p2, q2, p1):
        expected = True
    elif o4 == 0 and on_segment(p2, q2, q1):
        expected = True
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="geometric_01",
        name="Closest Pair of Points",
        category="geometric",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Given n points in 2D, find the pair with the smallest\n"
            "squared Euclidean distance. Brute-force O(n^2) for the\n"
            "test gauntlet; a real implementation would use divide and\n"
            "conquer for O(n log n). Return (distance^2, sorted pair).\n"
            "Source: https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/",
        params=["points", "n"],
        inputs={
            "points": "list of n (x, y) tuples.",
            "n": "number of points.",
        },
        returns="(squared_distance, [p1, p2]) - the pair and its squared distance.",
        source=GEO_01_SOURCE,
        setup_fn=_setup_closest_pair,
        verify_fn=_verify_closest_pair,
        samples=[
            Sample("points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)], n = 6", "((2, 3) and (3, 4), 2)"),
        ],
        hint="Brute force: check every pair. Real solution: divide and conquer on x-sorted points.",
        parents=["dc_03"],
        children=["geometric_02"],
    ),
    AlgorithmSpec(
        id="geometric_02",
        name="Convex Hull (Graham Scan)",
        category="geometric",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Return the convex hull of a set of 2D points as a sorted\n"
            "list. Graham scan: pick the bottom-most-leftmost point as\n"
            "the pivot, sort the rest by polar angle, walk the sorted\n"
            "list popping non-left turns. O(n log n).\n"
            "Source: https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/"
        ),
        source_url="https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/",
        params=["points", "n"],
        inputs={
            "points": "list of n (x, y) tuples (distinct).",
            "n": "number of points.",
        },
        returns="a sorted list of the hull points.",
        source=GEO_02_SOURCE,
        setup_fn=_setup_convex_hull,
        verify_fn=_verify_convex_hull,
        samples=[
            Sample("points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)], n = 7", "[(0,0), (1,1), (3,0), (3,3), (0,3)]"),
        ],
        hint="Bottom-most-leftmost pivot. Sort by polar angle. Pop non-left turns.",
        parents=["geometric_01"],
        children=["geometric_03"],
    ),
    AlgorithmSpec(
        id="geometric_03",
        name="Line Segment Intersection",
        category="geometric",
        difficulty=4,
        required_complexity=ComplexityClass.O_1,
        description=(
            "Return True iff two line segments intersect. The standard\n"
            "orientation test: the segments straddle each other iff\n"
            "the orientations of (p1, q1, p2) and (p1, q1, q2) have\n"
            "opposite signs, AND the orientations of (p2, q2, p1)\n"
            "and (p2, q2, q1) have opposite signs. Plus the collinear-\n"
            "on-segment edge cases.\n"
            "Source: https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/"
        ),
        source_url="https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/",
        params=["seg1", "seg2"],
        inputs={
            "seg1": "((x1, y1), (x2, y2)) - the first segment.",
            "seg2": "((x3, y3), (x4, y4)) - the second segment.",
        },
        returns="True iff the two segments intersect.",
        source=GEO_03_SOURCE,
        setup_fn=_setup_line_intersect,
        verify_fn=_verify_line_intersect,
        samples=[
            Sample("seg1 = ((1, 1), (10, 1)), seg2 = ((1, 2), (10, 2))", "False (parallel)"),
            Sample("seg1 = ((0, 0), (10, 10)), seg2 = ((0, 10), (10, 0))", "True (cross at (5, 5))"),
        ],
        hint="orient(a, b, c) = (b-a) x (c-a). The segments straddle iff orient(p1,q1,p2) and orient(p1,q1,q2) have opposite signs.",
        parents=["geometric_02"],
        children=[],
    ),
]
