"""Optimal solution for dc_16: Quickhull Convex Hull.

Given n points in the plane, return the vertices of
"""


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
