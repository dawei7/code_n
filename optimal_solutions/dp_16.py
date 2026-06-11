"""Optimal solution for dp_16: Egg Dropping.

dp[e][m] = max floors testable with e eggs and m moves.
Find smallest m with dp[k][m] >= n.
"""


def solve(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    m = 0
    while dp[k][m] < n:
        m += 1
        for e in range(1, k + 1):
            dp[e][m] = dp[e - 1][m - 1] + dp[e][m - 1] + 1
    return m
