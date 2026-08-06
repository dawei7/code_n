"""Proposed app-local solution for LeetCode 387."""


def solve(s: str) -> int:
    counts = [0] * 26
    base = ord("a")

    for character in s:
        counts[ord(character) - base] += 1

    for i, character in enumerate(s):
        if counts[ord(character) - base] == 1:
            return i

    return -1
