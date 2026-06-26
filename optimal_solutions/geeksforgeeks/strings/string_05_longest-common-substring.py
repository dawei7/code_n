"""Optimal solution for string_05: Longest Common Substring.

DP with a single rolling row. dp[i][j] = length of the longest
common suffix of s[:i] and t[:j].
"""


def solve(s, t):
    m, n = len(s), len(t)
    if m == 0 or n == 0:
        return 0
    prev = [0] * (n + 1)
    best = 0
    for i in range(1, m + 1):
        cur = [0] * (n + 1)
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best
