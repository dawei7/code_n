"""Optimal solution for string_14: Longest Repeating Subsequence.

dp[i][j] = LRS length of s[i..] and s[j..] (with i != j).
"""


def solve(s, n):
    if n == 0:
        return 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == s[j] and i != j:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]
