"""Optimal solution for LeetCode 3035: Maximum Palindromes After Operations."""

from collections import Counter


def solve(words: list[str]) -> int:
    frequencies = Counter(character for word in words for character in word)
    available_pairs = sum(count // 2 for count in frequencies.values())

    answer = 0
    for length in sorted(map(len, words)):
        required_pairs = length // 2
        if required_pairs > available_pairs:
            break
        available_pairs -= required_pairs
        answer += 1

    return answer
