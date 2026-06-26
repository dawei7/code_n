"""Optimal solution for dp_30: Coin Change (Count Ways).

dp[a] = number of ways to make a. For each coin c, walk
forward: dp[a] += dp[a - c].
"""


def solve(coins, n, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
