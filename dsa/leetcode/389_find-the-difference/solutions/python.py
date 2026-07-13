"""Optimal app-local solution for LeetCode 389: Find the Difference."""


def solve(s: str, t: str) -> str:
    unmatched = 0

    for character in s:
        unmatched ^= ord(character)
    for character in t:
        unmatched ^= ord(character)

    return chr(unmatched)
