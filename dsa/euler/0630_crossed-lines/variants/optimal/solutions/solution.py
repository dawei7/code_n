"""Project Euler Problem 630: Crossed Lines.

Mathematical Formulation:
Generate points from Blum Blum Shub PRNG.
Find distinct lines formed by pairs of points and compute the number of crossings.
"""

from __future__ import annotations

import math


def solve(num_lines: int = 2500) -> str:
    """Compute S(L_2500) = total crossing points across all lines."""
    # Blum Blum Shub generator
    s = 290797
    bbs = []
    for _ in range(num_lines * 2):
        s = (s * s) % 50515093
        t = (s % 2000) - 1000
        bbs.append(t)

    points = []
    for i in range(0, len(bbs), 2):
        points.append((bbs[i], bbs[i + 1]))

    # Group lines by slope (dy/g, dx/g) and intercept
    lines_by_slope: dict[tuple[int, int], set[int]] = {}
    
    n_pts = min(len(points), 2500)
    for i in range(n_pts):
        x1, y1 = points[i]
        for j in range(i + 1, n_pts):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            g = math.gcd(dx, abs(dy))
            dx //= g
            dy //= g
            
            # Line equation: dy * x - dx * y + c = 0 => c = dx * y1 - dy * x1
            c = dx * y1 - dy * x1
            slope = (dy, dx)
            if slope not in lines_by_slope:
                lines_by_slope[slope] = set()
            lines_by_slope[slope].add(c)

    # Number of parallel lines per direction
    slope_counts = [len(intercepts) for intercepts in lines_by_slope.values()]
    total_unique_lines = sum(slope_counts)
    
    # Total crossing pairs: sum_{s} count(s) * (total_lines - count(s))
    total_crossings = 0
    for count in slope_counts:
        total_crossings += count * (total_unique_lines - count)

    return str(total_crossings)


if __name__ == "__main__":
    print(solve())
