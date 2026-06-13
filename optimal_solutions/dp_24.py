"""Optimal solution for dp_24: Palindromic Partitioning (Min Cuts).

Return the minimum number of cuts to partition s into
palindromes. Precompute is_pal[i][j] (whether s[i..j] is a
palindrome) in O(n^2), then dp[i] = min over j with
is_pal[i][j] of (0 if j == n-1 else 1 + dp[j+1]).
"""


def solve(s, n):
    if n == 0:
        return 0
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if is_pal[i][j]:
                cost = 0 if j == n - 1 else 1 + dp[j + 1]
                if cost < dp[i]:
                    dp[i] = cost
    return dp[0]
