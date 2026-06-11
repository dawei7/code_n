"""Optimal solution for dp_14: Palindromic Partitioning.

Min cuts to partition a string into all-palindromic substrings.
"""


def solve(s):
    n = len(s)
    if n <= 1:
        return 0
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True
    INF = float("inf")
    dp = [INF] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_pal[j + 1][i] and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
    return dp[n - 1]
