"""Optimal solution for string_11: Longest Common Substring.

Length of the longest common substring (consecutive, not
subsequence) of s1 and s2. Standard DP: dp[i][j] = length
of the common suffix of s1[..i] and s2[..j]. The answer
is the max over the table.
"""


def solve(s1, s2, n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    best = 0
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > best:
                    best = dp[i][j]
            else:
                dp[i][j] = 0
    return best
