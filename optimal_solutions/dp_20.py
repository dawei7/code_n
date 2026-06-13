"""Optimal solution for dp_20: Shortest Common Supersequence (Length).

The shortest string that has both s1 and s2 as subsequences.
The length is n1 + n2 - LCS(s1, s2). Compute LCS first, then
combine the lengths.
"""


def solve(s1, s2, n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    lcs = dp[n1][n2]
    return n1 + n2 - lcs
