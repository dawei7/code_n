"""Optimal solution for dp_04: Longest Common Subsequence.

DP table: dp[i][j] = LCS length of seq_a[:i] and seq_b[:j]. O(n*m)
time, O(n*m) space.
"""


def solve(seq_a, seq_b):
    m, n = len(seq_a), len(seq_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq_a[i - 1] == seq_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
