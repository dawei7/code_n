"""Optimal solution for geometric_01: Closest Pair of Points.

Brute-force O(n^2) for the test gauntlet. Check every pair;
return the smallest squared distance and the sorted pair.
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
