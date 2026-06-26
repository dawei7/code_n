"""Optimal solution for string_10: Word Break.

True iff s can be segmented into a sequence of dictionary words.
"""


def solve(s, word_dict):
    n = len(s)
    word_set = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
