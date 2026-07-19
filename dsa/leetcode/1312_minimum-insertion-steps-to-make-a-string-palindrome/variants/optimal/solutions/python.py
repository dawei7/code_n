"""Optimal app-local solution for LeetCode 1312."""


def solve(s):
    n = len(s)
    dp = [0] * n

    for left in range(n - 2, -1, -1):
        diagonal = 0
        for right in range(left + 1, n):
            below = dp[right]
            if s[left] == s[right]:
                dp[right] = diagonal
            else:
                dp[right] = 1 + min(dp[right], dp[right - 1])
            diagonal = below

    return dp[-1]
