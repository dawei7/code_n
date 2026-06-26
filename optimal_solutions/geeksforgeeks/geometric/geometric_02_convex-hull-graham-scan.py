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
    pivot = min(points)

    def angle_key(p):
        if p == pivot:
            return (-math.inf,)
        dx = p[0] - pivot[0]
        dy = p[1] - pivot[1]
        return (math.atan2(dy, dx), dx * dx + dy * dy)

    rest = [p for p in points if p != pivot]
    rest.sort(key=angle_key)
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
