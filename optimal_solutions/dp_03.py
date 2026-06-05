"""Optimal solution for dp_03: 0/1 Knapsack.

Classic DP table: dp[i][c] = max value using the first i items
with capacity c. O(n * capacity) time, O(n * capacity) space.
"""


def solve(weights, values, capacity, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][capacity]
