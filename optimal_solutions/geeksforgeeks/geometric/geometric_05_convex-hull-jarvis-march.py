"""Optimal solution for geometric_05: Convex Hull (Jarvis March).

Compute the convex hull of n points using Jarvis
"""


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
