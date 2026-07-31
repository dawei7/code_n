"""Optimal app-local solution for LeetCode 939."""


def solve(points):
    point_set = {tuple(point) for point in points}
    best = None
    for first in range(len(points)):
        x1, y1 = points[first]
        for second in range(first + 1, len(points)):
            x2, y2 = points[second]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in point_set and (x2, y1) in point_set:
                area = abs(x1 - x2) * abs(y1 - y2)
                if best is None or area < best:
                    best = area
    return 0 if best is None else best
