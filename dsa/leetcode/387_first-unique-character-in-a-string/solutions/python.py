"""Optimal app-local solution for LeetCode 387: First Unique Character in a String."""


def solve(s: str) -> int:
    counts = [0] * 26
    base = ord("a")

    for character in s:
        counts[ord(character) - base] += 1

    for index, character in enumerate(s):
        if counts[ord(character) - base] == 1:
            return index

    return -1
