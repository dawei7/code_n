"""Optimal app-local solution for LeetCode 884."""

from collections import Counter


def solve(s1, s2):
    frequencies = Counter(s1.split())
    frequencies.update(s2.split())
    return [word for word, count in frequencies.items() if count == 1]
