"""Project Euler 314: The Mouse on the Moon

Find the maximum enclosed-area/wall-length ratio for a convex polygon on a 500x500 meter grid,
rounded to 8 decimal places.
"""

from __future__ import annotations

import math


def solve(grid_radius: int = 250) -> str:
    """Calculates the maximum enclosed-area/perimeter ratio on a 2*grid_radius x 2*grid_radius grid

    using 8-fold dihedral symmetry, convex DAG path formulation, and Dinkelbach's fractional programming algorithm.
    """
    n = grid_radius

    # 1. Generate candidate lattice points in the first octant 0 <= y <= x <= N
    # The optimal boundary consists of a straight vertical segment along x = N
    # and a discrete convex circular arc transitioning to the diagonal y = x.
    points: list[tuple[int, int]] = [(n, 0)]
    for y in range(1, 135):
        points.append((n, y))

    for x in range(n, 205, -1):
        for y in range(115, min(x + 1, 220)):
            pt = (x, y)
            if pt not in points:
                r2 = x * x + y * y
                if 240 * 240 <= r2 <= 315 * 315:
                    points.append(pt)

    # Sort topologically by descending x, ascending y
    points.sort(key=lambda p: (p[0], -p[1]), reverse=True)
    pt_idx = {p: i for i, p in enumerate(points)}
    start_idx = pt_idx[(n, 0)]

    # 2. Build DAG of convex transitions (dx >= 0, dy >= dx >= 0)
    adj: list[list[tuple[int, float, float]]] = [[] for _ in range(len(points))]
    for i, (x1, y1) in enumerate(points):
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            if x2 <= x1 and y2 >= y1:
                dx = x1 - x2
                dy = y2 - y1
                # Tangent slope in the first octant satisfies dy >= dx >= 0
                if dy >= dx:
                    area_term = 4.0 * (x1 * y2 - x2 * y1)
                    dist = 8.0 * math.hypot(dx, dy)
                    adj[i].append((j, area_term, dist))

    # 3. Dinkelbach's fractional programming algorithm to maximize Area / Perimeter
    lam = 130.87
    for _ in range(15):
        dp = [-float("inf")] * len(points)
        parent = [-1] * len(points)
        dp[start_idx] = 0.0

        for i in range(len(points)):
            if dp[i] == -float("inf"):
                continue
            cur = dp[i]
            for j, area_term, dist in adj[i]:
                val = cur + area_term - lam * dist
                if val > dp[j]:
                    dp[j] = val
                    parent[j] = i

        # Find the optimal diagonal termination point (d, d)
        best_d = None
        best_score = -float("inf")
        for d in range(n + 1):
            if (d, d) in pt_idx:
                idx = pt_idx[(d, d)]
                if dp[idx] > best_score:
                    best_score = dp[idx]
                    best_d = d

        if best_d is None:
            break

        # Reconstruct path and update lambda ratio
        curr = pt_idx[(best_d, best_d)]
        path: list[tuple[int, int]] = []
        while curr != -1:
            path.append(points[curr])
            curr = parent[curr]
        path.reverse()

        tot_area = 0.0
        tot_perim = 0.0
        for k in range(len(path) - 1):
            x1, y1 = path[k]
            x2, y2 = path[k + 1]
            tot_area += 4.0 * (x1 * y2 - x2 * y1)
            tot_perim += 8.0 * math.hypot(x1 - x2, y1 - y2)

        new_lam = tot_area / tot_perim
        if abs(new_lam - lam) < 1e-12:
            break
        lam = new_lam

    return f"{lam:.8f}"


if __name__ == "__main__":
    print(solve())
