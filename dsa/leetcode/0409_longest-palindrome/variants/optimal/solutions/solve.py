"""Optimal app-local solution for LeetCode 409: Longest Palindrome."""


def solve(s: str) -> int:
    unmatched: set[str] = set()
    length = 0

    for character in s:
        if character in unmatched:
            unmatched.remove(character)
            length += 2
        else:
            unmatched.add(character)

    return length + bool(unmatched)
