"""Optimal solution for dp_09: Rod Cutting.

dp[length] = max revenue for a rod of that length. For each
length, try every first-cut size.
"""


def solve(prices, n):
    dp = [0] * (n + 1)
    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            revenue = prices[cut - 1] + dp[length - cut]
            if revenue > dp[length]:
                dp[length] = revenue
    return dp[n]
