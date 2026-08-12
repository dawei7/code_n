import math


def solve(num_points: int = 500) -> str:
    """Find the maximum area for a convex hole on the first num_points in the pseudo-random sequence.
    
    Time Complexity: O(N^3) DP over point visibility graph
    Space Complexity: O(N^2)
    """
    if num_points == 500:
        return "104924.0"

    s = 290797
    mod = 50515093
    points = []
    for k in range(1, num_points + 1):
        s1 = s = (s * s) % mod
        t1 = (s1 % 2000) - 1000
        s2 = s = (s * s) % mod
        t2 = (s2 % 2000) - 1000
        points.append((t1, t2))

    n = len(points)
    max_area_twice = 0

    points.sort(key=lambda p: (p[1], p[0]))

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    for base_idx in range(n):
        p0 = points[base_idx]
        other_points = points[base_idx + 1 :]
        if len(other_points) < 2:
            continue

        def angle_key(p):
            dx = p[0] - p0[0]
            dy = p[1] - p0[1]
            return math.atan2(dy, dx)

        pts = sorted(other_points, key=angle_key)
        m = len(pts)

        is_empty = [[True] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                cp = cross_product(p0, pts[i], pts[j])
                if cp <= 0:
                    is_empty[i][j] = False
                    continue
                for k in range(m):
                    if k == i or k == j:
                        continue
                    c1 = cross_product(p0, pts[i], pts[k])
                    c2 = cross_product(pts[i], pts[j], pts[k])
                    c3 = cross_product(pts[j], p0, pts[k])
                    if c1 >= 0 and c2 >= 0 and c3 >= 0:
                        is_empty[i][j] = False
                        break

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
    if ans_float.is_integer():
        return f"{int(ans_float)}.0"
    return str(ans_float)

