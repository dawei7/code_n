"""Optimal solution for LeetCode 3029: Minimum Time to Revert Word to Initial State I."""


def solve(word: str, k: int) -> int:
    n = len(word)

    for removed in range(k, n, k):
        if word[removed:] == word[: n - removed]:
            return removed // k

    return (n + k - 1) // k
