"""Project Euler 270: Cutting Squares

Find C(30) mod 10^8, the number of ways to cut an N x N square (N=30) into triangles
using straight non-crossing cuts between integer boundary points on different sides.
"""

from __future__ import annotations


def solve(n: int = 30, mod: int = 10**8) -> str:
    """Calculates C(N) mod 10^8 using constrained polygon triangulation dynamic programming

    over the 4N border vertices of the square.
    """
    total_vertices = 4 * n

    def same_side(u: int, v: int) -> bool:
        if 0 <= u <= n and 0 <= v <= n:
            return True
        if n <= u <= 2 * n and n <= v <= 2 * n:
            return True
        if 2 * n <= u <= 3 * n and 2 * n <= v <= 3 * n:
            return True
        if (3 * n <= u <= 4 * n or u == 0) and (
            3 * n <= v <= 4 * n or v == 0
        ):
            return True
        return False

    # dp[i][j] stores the number of valid triangulations for the subpolygon on boundary vertices i..j
    dp = [[0] * (total_vertices + 1) for _ in range(total_vertices + 1)]
    for i in range(total_vertices):
        dp[i][i + 1] = 1

    # Dynamic programming across interval lengths L = 2 .. 4N-1
    for length in range(2, total_vertices):
        for i in range(0, total_vertices - length + 1):
            j = i + length
            ways = 0
            for k in range(i + 1, j):
                if k > i + 1 and same_side(i, k):
                    continue
                if k < j - 1 and same_side(k, j):
                    continue
                ways = (ways + dp[i][k] * dp[k][j]) % mod
            dp[i][j] = ways

    # Form triangles containing the base boundary edge (0, total_vertices - 1)
    total_triangulations = 0
    for k in range(1, total_vertices - 1):
        if k > 1 and same_side(0, k):
            continue
        if k < total_vertices - 2 and same_side(k, total_vertices - 1):
            continue
        total_triangulations = (
            total_triangulations + dp[0][k] * dp[k][total_vertices - 1]
        ) % mod

    return str(total_triangulations)


if __name__ == "__main__":
    print(solve())
