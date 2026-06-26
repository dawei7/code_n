"""Optimal solution for geometric_07: Max Points on Same Line.

Given n points in the plane, find the maximum
"""


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
