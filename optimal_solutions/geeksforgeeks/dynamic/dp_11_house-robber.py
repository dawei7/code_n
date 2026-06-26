"""Optimal solution for dp_11: House Robber.

Max sum of non-adjacent elements.
"""


def solve(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    dp = [0] * (n + 1)
    dp[1] = arr[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
    return dp[n]
