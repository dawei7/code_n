"""Optimal app-local solution for LeetCode 424."""


def solve(s: str, k: int) -> int:
    frequencies = [0] * 26
    left = 0
    best = 0

    for right, character in enumerate(s):
        frequencies[ord(character) - ord("A")] += 1
        while right - left + 1 - max(frequencies) > k:
            frequencies[ord(s[left]) - ord("A")] -= 1
            left += 1
        best = max(best, right - left + 1)

    return best
