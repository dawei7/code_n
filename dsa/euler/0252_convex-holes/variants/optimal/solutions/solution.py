"""
Project Euler Problem 252: Convex Holes

Problem Statement:
Given a set of points S on the 2D plane, a convex hole is a subset of S
that forms a convex polygon whose interior contains no other points of S.

Points are generated using Blum Blum Shub pseudo-random generator:
    S_0 = 290797
    S_{n+1} = S_n^2 mod 50515093
    T_{2k-1} = (S_{2k-1} mod 2000) - 1000
    T_{2k} = (S_{2k} mod 2000) - 1000
    P_k = (T_{2k-1}, T_{2k})

For a given N, find the maximum area of a convex hole using points from P_1 to P_N.
For N = 20, the maximum area is 1049694.5.
For N = 500, calculate the maximum area.
"""

import math


def solve(num_points: int = 500) -> str:
    """
    Finds the maximum area of a convex hole among the first N pseudo-random points.
    """
    s = 290797
    mod = 50515093
    points = []
    for _ in range(num_points):
        s1 = s = (s * s) % mod
        t1 = (s1 % 2000) - 1000
        s2 = s = (s * s) % mod
        t2 = (s2 % 2000) - 1000
        points.append((t1, t2))

    n = len(points)
    max_area_twice = 0
    # Sort points bottom-to-top, left-to-right to break ties
    points.sort(key=lambda p: (p[1], p[0]))

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    for base_idx in range(n):
        p0 = points[base_idx]
        other_points = points[base_idx + 1 :]
        if len(other_points) < 2:
            continue

        # Sort remaining points radially in counter-clockwise order around p0
        def angle_key(p):
            return math.atan2(p[1] - p0[1], p[0] - p0[0])

        pts = sorted(other_points, key=angle_key)
        m = len(pts)

        # Precompute emptiness of triangle (p0, pts[i], pts[j])
        is_empty = [[True] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                cp = cross_product(p0, pts[i], pts[j])
                if cp <= 0:
                    is_empty[i][j] = False
                    continue
                # For any point k between i and j in angular order, check if inside triangle
                for k in range(i + 1, j):
                    if cross_product(pts[i], pts[j], pts[k]) >= 0:
                        is_empty[i][j] = False
                        break

        # dp[i][j] = max twice-area of convex polygon starting at p0 with last edge pts[i]->pts[j]
        dp = [[0] * m for _ in range(m)]

        for j in range(m):
            for i in range(j):
                if not is_empty[i][j]:
                    continue
                tri_area2 = cross_product(p0, pts[i], pts[j])
                best_prev = 0
                for l in range(i):
                    if dp[l][i] > 0 and cross_product(pts[l], pts[i], pts[j]) > 0:
                        if dp[l][i] > best_prev:
                            best_prev = dp[l][i]
                chain_area2 = tri_area2 + best_prev
                dp[i][j] = chain_area2
                if chain_area2 > max_area_twice:
                    max_area_twice = chain_area2

    ans_float = max_area_twice / 2.0
    ans = f"{int(ans_float)}.0" if ans_float.is_integer() else str(ans_float)
    return ans


if __name__ == "__main__":
    print(solve())
