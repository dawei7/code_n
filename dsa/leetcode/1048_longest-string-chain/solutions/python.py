"""Optimal solution for LeetCode 1048: Longest String Chain."""


def solve(words: list[str]) -> int:
    dp: dict[str, int] = {}
    best = 1
    for word in sorted(words, key=len):
        longest = 1
        for i in range(len(word)):
            predecessor = word[:i] + word[i + 1 :]
            longest = max(longest, dp.get(predecessor, 0) + 1)
        dp[word] = longest
        best = max(best, longest)
    return best
