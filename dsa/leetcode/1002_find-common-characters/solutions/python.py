"""Optimal solution for LeetCode 1002: Find Common Characters."""

from collections import Counter


def solve(words: list[str]) -> list[str]:
    common = Counter(words[0])
    for word in words[1:]:
        common &= Counter(word)

    answer: list[str] = []
    for char in sorted(common):
        answer.extend([char] * common[char])
    return answer
