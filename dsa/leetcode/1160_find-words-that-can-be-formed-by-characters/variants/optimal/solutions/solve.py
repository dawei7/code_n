"""Optimal app-local solution for LeetCode 1160."""

from collections import Counter


def solve(words: list[str], chars: str) -> int:
    available = Counter(chars)
    answer = 0
    for word in words:
        required = Counter(word)
        if all(count <= available[letter] for letter, count in required.items()):
            answer += len(word)
    return answer
