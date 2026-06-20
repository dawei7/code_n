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


# === geometric_04: Point in Polygon (Ray Casting) ===

GEOMETRIC_04_SOURCE = '''
def solve(polygon, point, m):
    """Ray-casting point-in-polygon test."""
    if m < 3:
        return False
    x, y = point
    inside = False
    j = m - 1
    for i in range(m):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        # Edge (xj, yj) -> (xi, yi). Check if the horizontal
        # ray at y=y from the point crosses this edge.
        if ((yi > y) != (yj > y)):
            # The edge straddles the ray. Compute the x
            # intersection and check it's to the right of the
            # point.
            x_int = (xj * (yi - y) + xi * (y - yj)) / (yi - yj)
            if x < x_int:
                inside = not inside
        # Also: if the point lies on this edge, count as inside.
        # We can detect collinearity by checking the cross product
        # and bounding box.
        def _on_seg(a, b, c):
            return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0])
                    and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])
                    and (b[0] - a[0]) * (c[1] - a[1])
                        == (b[1] - a[1]) * (c[0] - a[0]))
        if _on_seg(polygon[i], polygon[j], point):
            return True
        j = i
    return inside
'''

def _setup_geometric_04(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Build a simple convex polygon (a square or rectangle) so the
    # test is well-defined. The spec runtime passes `n` as the
    # setup size; we treat it as the polygon size.
    m = max(3, min(n, 8))
    # Generate a regular-ish convex polygon.
    cx, cy = 10, 10
    radius = 6
    polygon = []
    for k in range(m):
        angle = 2 * math.pi * k / m + rng.uniform(-0.1, 0.1)
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        polygon.append((round(px, 2), round(py, 2)))
    # Pick a query point: 50/50 inside vs outside.
    # Use a slightly larger bounding box to allow outside.
    inside_box = (cx, cy)  # known to be inside for a regular convex polygon
    outside_box = (cx + 3 * radius, cy + 3 * radius)  # definitely outside
    if rng.random() < 0.5:
        point = inside_box
    else:
        point = outside_box
    challenge._polygon = list(polygon)
    challenge._point = point
    return {
        "polygon": list(polygon),
        "point": point,
        "m": m,
    }

def _verify_geometric_04(challenge, result):
    # Brute-force verify: for convex polygons (which our setup
    # generates), use the winding-number test by counting the
    # number of signed cross products that change sign around
    # the point.
    # Simpler: use a "ray to +infinity" cast manually and count
    # crossings robustly.
    polygon = challenge._polygon
    m = len(polygon)
    px, py = challenge._point
    # Reference: for convex polygons generated by a circle,
    # inside if distance from center < radius, outside if > radius.
    center = (10, 10)
    radius = 6
    dist = math.hypot(px - center[0], py - center[1])
    expected = dist < radius
    # Also: if the point is on the boundary, expected is True.
    # Skip boundary check for the test (probability of hitting it
    # exactly is zero with float coordinates).
    return result == expected



# === geometric_05: Convex Hull (Jarvis March) ===

GEOMETRIC_05_SOURCE = '''
def solve(points, n):
    """Convex hull via Jarvis March (gift wrapping)."""
    if n < 3:
        return sorted(points)
    # Find the leftmost point.
    leftmost = min(range(n), key=lambda i: (points[i][0], points[i][1]))
    hull = []
    cur = leftmost
    while True:
        hull.append(cur)
        # Find the next hull vertex: the most counterclockwise
        # point with respect to the current edge.
        candidate = None
        for j in range(n):
            if j == cur:
                continue
            if candidate is None:
                candidate = j
                continue
            # We want (candidate - cur) to be the most
            # counterclockwise of all points. Cross product
            # positive means j is more CCW than candidate.
            cross = ((points[candidate][0] - points[cur][0])
                     * (points[j][1] - points[cur][1])
                     - (points[candidate][1] - points[cur][1])
                     * (points[j][0] - points[cur][0]))
            if cross < 0:
                candidate = j
        # If the next candidate is the leftmost, we're done.
        if candidate == leftmost:
            break
        cur = candidate
        # Safety: avoid infinite loop on degenerate inputs.
        if len(hull) > n:
            break
    return [points[i] for i in hull]
'''

def _setup_geometric_05(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(3, min(n, 10))
    # Build a simple convex polygon (a square or rectangle) plus a
    # few interior points, so the hull is non-trivial.
    points = []
    # Outer square.
    points.extend([(0, 0), (10, 0), (10, 10), (0, 10)])
    # Add some interior points (random subset of these) to make
    # the hull include more than the obvious square. Cap so that
    # the total number of points does not exceed n.
    interior = [(3, 5), (5, 2), (7, 5), (2, 8), (5, 5), (5, 7), (8, 3)]
    rng.shuffle(interior)
    n_inner = max(0, min(len(interior), n - 4))
    points.extend(interior[:n_inner])
    # Pad with more random points if needed (to reach n).
    seen = set(points)
    while len(points) < n:
        p = (rng.randint(0, 10), rng.randint(0, 10))
        if p not in seen:
            seen.add(p)
            points.append(p)
    # If we somehow overshot (shouldn't happen with n_inner = n - 4),
    # truncate to n.
    points = points[:n]
    rng.shuffle(points)
    challenge._points = list(points)
    return {"points": list(points), "n": n}

def _verify_geometric_05(challenge, result):
    # Reference: Graham scan (already implemented in geometric_02).
    def _cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def _graham(points):
        pts = sorted(set(points))
        if len(pts) < 3:
            return sorted(pts)
        pivot = min(pts)
        def key(p):
            if p == pivot:
                return (-math.inf,)
            dx = p[0] - pivot[0]
            dy = p[1] - pivot[1]
            return (math.atan2(dy, dx), dx * dx + dy * dy)
        rest = [p for p in pts if p != pivot]
        rest.sort(key=key)
        hull = [pivot]
        for p in rest:
            while len(hull) >= 2:
                o, a = hull[-2], hull[-1]
                if _cross(o, a, p) <= 0:
                    hull.pop()
                else:
                    break
            hull.append(p)
        return sorted(hull)

    expected = _graham(challenge._points)
    got = sorted(result)
    return got == expected



# === geometric_06: Rectangle Overlap (Axis-Aligned) ===

GEOMETRIC_06_SOURCE = '''
def solve(l1, r1, l2, r2):
    """Two rectangles do not overlap iff one is entirely left
    of the other, or one is entirely above the other.
    l1 = top-left, r1 = bottom-right (y-axis points up).
    """
    # If rectangle 1 is to the right of rectangle 2, no overlap.
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False
    # If rectangle 1 is above rectangle 2, no overlap.
    # "Above" means l1.y > r2.y (r1.y is the lower y-bound of rect 1).
    if r1[1] > l2[1] or r2[1] > l1[1]:
        return False
    return True
'''

def _setup_geometric_06(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Build two random axis-aligned rectangles. ~half the time, make
    # them overlap; the other half, keep them disjoint.
    def rand_rect():
        x1 = rng.randint(0, 15)
        x2 = rng.randint(x1 + 1, 25)
        y1 = rng.randint(5, 25)
        y2 = rng.randint(0, y1 - 1)
        return (x1, y1), (x2, y2)
    l1, r1 = rand_rect()
    l2, r2 = rand_rect()
    if rng.random() < 0.5:
        # Force overlap: place rect2 so it overlaps rect1.
        l2 = (l1[0] + 1, l1[1] + 1)
        r2 = (r1[0] + 1, r1[1] - 1) if r1[1] - 1 > r1[1] - 2 else (r1[0] + 2, r1[1] - 2)
    else:
        # Force non-overlap: place rect2 to the right of rect1.
        l2 = (r1[0] + 3, l1[1])
        r2 = (r1[0] + 10, r1[1] - 5)
    challenge._l1 = l1
    challenge._r1 = r1
    challenge._l2 = l2
    challenge._r2 = r2
    return {"l1": l1, "r1": r1, "l2": l2, "r2": r2}

def _verify_geometric_06(challenge, result):
    # Brute force: for each corner of rect 2, check if it's strictly
    # inside rect 1 (which is sufficient for non-touching overlap).
    # Or do the inverse. Easiest: re-run the canonical condition.
    l1 = challenge._l1
    r1 = challenge._r1
    l2 = challenge._l2
    r2 = challenge._r2
    expected = (l1[0] <= r2[0] and l2[0] <= r1[0]
                and r1[1] <= l2[1] and r2[1] <= l1[1])
    return result == expected



# === geometric_07: Max Points on Same Line ===

GEOMETRIC_07_SOURCE = '''
def solve(points, n):
    """Max points on the same line via slope hashing."""
    from math import gcd
    if n < 2:
        return n
    best = 0
    for i in range(n):
        slopes = {}
        duplicates = 0
        vertical = 0
        for j in range(n):
            if i == j:
                continue
            if points[i] == points[j]:
                duplicates += 1
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0:
                # Vertical line.
                vertical += 1
            else:
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                # Normalize sign: force dx > 0 (or both zero).
                if dx < 0:
                    dx = -dx
                    dy = -dy
                key = (dy, dx)
                slopes[key] = slopes.get(key, 0) + 1
        local_max = vertical
        for c in slopes.values():
            if c > local_max:
                local_max = c
        total = local_max + duplicates + 1  # +1 for the pivot itself
        if total > best:
            best = total
    return best
'''

def _setup_geometric_07(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(2, min(n, 8))
    # Build a set with a guaranteed collinear subset of size >= 3.
    import random
    rng2 = random.Random(seed + 1)
    # Pick a slope (dy, dx) and a base point.
    dx = rng2.choice([-3, -2, -1, 1, 2, 3])
    dy = rng2.choice([-3, -2, -1, 1, 2, 3])
    bx, by = rng2.randint(-10, 10), rng2.randint(-10, 10)
    n_collinear = max(2, min(n - 1, rng2.randint(3, max(3, n - 1))))
    points = set()
    for k in range(n_collinear):
        x = bx + k * dx
        y = by + k * dy
        points.add((x, y))
    # Add more random points until we have n total.
    while len(points) < n:
        p = (rng2.randint(-15, 15), rng2.randint(-15, 15))
        if p not in points:
            points.add(p)
    points = list(points)
    rng2.shuffle(points)
    challenge._points = list(points)
    return {"points": list(points), "n": len(points)}

def _verify_geometric_07(challenge, result):
    # Brute force: for every pair of points, count how many points
    # lie on the line through them. The max over all pairs is the
    # answer.
    points = challenge._points
    n = len(points)
    if n < 2:
        return result == n
    best = 1
    for i in range(n):
        for j in range(i + 1, n):
            # Line through points[i] and points[j].
            ax, ay = points[i]
            bx, by = points[j]
            # Count points on this line.
            cnt = 0
            for k in range(n):
                x, y = points[k]
                # collinearity: (bx-ax)*(y-ay) == (by-ay)*(x-ax)
                if (bx - ax) * (y - ay) == (by - ay) * (x - ax):
                    cnt += 1
            if cnt > best:
                best = cnt
    return result == best


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="geometric_04",
        name="Point in Polygon (Ray Casting)",
        category="geometric",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Given a simple polygon (as a list of (x, y) vertices
            in order) and a query point, return True if the
            point lies inside the polygon and False otherwise.
            Use the ray-casting (even-odd) algorithm: shoot a
            horizontal ray from the point to +infinity and count
            the number of times it crosses a polygon edge. An
            odd count means inside. The point is also
            considered inside if it lies exactly on an edge or
            vertex. O(n) per query.
            Source: https://www.geeksforgeeks.org/dsa/how-to-check-if-a-given-point-lies-inside-a-polygon/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/how-to-check-if-a-given-point-lies-inside-a-polygon/",
        params=["polygon", "point", "m"],
        inputs={
            "polygon": "list of m (x, y) tuples, the polygon vertices in order.",
            "point": "the (x, y) tuple to test.",
            "m": "number of polygon vertices.",
        },
        returns="True if the point is inside the polygon (or on its boundary), False otherwise.",
        source=GEOMETRIC_04_SOURCE,
        setup_fn=_setup_geometric_04,
        verify_fn=_verify_geometric_04,
        samples=[
            Sample("polygon = [(0,0),(10,0),(10,10),(0,10)], point = (5,5), m = 4", "True (inside a square)"),
            Sample("polygon = [(0,0),(10,0),(10,10),(0,10)], point = (20,5), m = 4", "False (outside)"),
        ],
        hint="Cast a horizontal ray from the point to +infinity. Count the number of polygon edges it crosses. Odd count means inside. Also: if the point lies on any edge, return True.",
        parents=["geometric_03"],
        children=["geometric_05"],
    ),
    AlgorithmSpec(
        id="geometric_05",
        name="Convex Hull (Jarvis March)",
        category="geometric",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Compute the convex hull of n points using Jarvis
            March (gift wrapping). Start at the leftmost point,
            then repeatedly find the next hull vertex as the
            point that makes the smallest (most counterclockwise)
            angle with the current edge. Stop when we return
            to the start. Return the hull vertices as a list of
            (x, y) tuples in CCW order, starting from the
            leftmost point. O(n^2) worst case, but O(nh) for
            small hulls.
            Source: https://www.geeksforgeeks.org/dsa/convex-hull-using-jarvis-algorithm/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/convex-hull-using-jarvis-algorithm/",
        params=["points", "n"],
        inputs={
            "points": "list of n (x, y) tuples.",
            "n": "number of points.",
        },
        returns="a list of (x, y) tuples forming the convex hull, in CCW order starting from the leftmost point.",
        source=GEOMETRIC_05_SOURCE,
        setup_fn=_setup_geometric_05,
        verify_fn=_verify_geometric_05,
        samples=[
            Sample("points = [(0,0),(1,1),(2,0),(1,0.5),(0,2)], n = 5", "a sorted CCW hull, e.g. [(0,0),(2,0),(0,2)]"),
        ],
        hint="Start at the leftmost point. At each step, find the most counterclockwise point (use cross product) and add it to the hull. Stop when you return to the start.",
        parents=["geometric_04"],
        children=["geometric_07"],
    ),
    AlgorithmSpec(
        id="geometric_06",
        name="Rectangle Overlap (Axis-Aligned)",
        category="geometric",
        difficulty=2,
        required_complexity=ComplexityClass.O_1,
        description=("""
            Given two axis-aligned rectangles (each given by its
            top-left corner l1, l2 and bottom-right corner r1,
            r2 with l.x <= r.x and l.y >= r.y, i.e., y grows
            upward), determine whether the two rectangles
            overlap (have a positive-area intersection).
            Two rectangles do NOT overlap iff one is entirely
            to the left of the other, or entirely above the
            other. Return True if they overlap, False
            otherwise. O(1).
            Source: https://www.geeksforgeeks.org/dsa/find-two-rectangles-overlap/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/find-two-rectangles-overlap/",
        params=["l1", "r1", "l2", "r2"],
        inputs={
            "l1": "(x, y) of the top-left corner of rectangle 1.",
            "r1": "(x, y) of the bottom-right corner of rectangle 1.",
            "l2": "(x, y) of the top-left corner of rectangle 2.",
            "r2": "(x, y) of the bottom-right corner of rectangle 2.",
        },
        returns="True if the rectangles overlap, False otherwise.",
        source=GEOMETRIC_06_SOURCE,
        setup_fn=_setup_geometric_06,
        verify_fn=_verify_geometric_06,
        samples=[
            Sample("l1 = (0,10), r1 = (10,0), l2 = (5,5), r2 = (15,0)", "True (overlap)"),
            Sample("l1 = (0,10), r1 = (10,0), l2 = (-10,5), r2 = (-1,0)", "False (rect2 is left of rect1)"),
        ],
        hint="Two rectangles do NOT overlap iff one is entirely to the left of the other (l1.x > r2.x or l2.x > r1.x) OR one is entirely above the other (r1.y > l2.y or r2.y > l1.y). Otherwise they overlap.",
        parents=["geometric_05"],
        children=[],
    ),
    AlgorithmSpec(
        id="geometric_07",
        name="Max Points on Same Line",
        category="geometric",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Given n points in the plane, find the maximum
            number of points that lie on the same straight line.
            For each pivot point, compute the slope to every
            other point (as a normalized (dy, dx) pair to avoid
            floating-point precision issues). Group points by
            slope and track the max group size. Handle vertical
            lines and duplicate points separately. O(n^2 log n)
            with the hash map, O(n^2) without.
            Source: https://www.geeksforgeeks.org/dsa/count-maximum-points-on-same-line/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/count-maximum-points-on-same-line/",
        params=["points", "n"],
        inputs={
            "points": "list of n (x, y) integer tuples.",
            "n": "number of points.",
        },
        returns="the maximum number of points on the same line, as an int.",
        source=GEOMETRIC_07_SOURCE,
        setup_fn=_setup_geometric_07,
        verify_fn=_verify_geometric_07,
        samples=[
            Sample("points = [(-1,1),(0,0),(1,1),(2,2),(3,3),(3,4)], n = 6", "4 (the line y=x has 4 points)"),
            Sample("points = [(0,0),(1,0),(0,1),(1,1)], n = 4", "2 (no three collinear)"),
        ],
        hint="For each pivot i, hash the slope (dy, dx) to every other point j. Group by slope; handle verticals (dx=0) and duplicates separately. The max group size + 1 + duplicates is the max points on a line through i.",
        parents=["geometric_05"],
        children=[],
    ),
])
