"""Optimal app-local solution for LeetCode 383: Ransom Note."""


def solve(ransom_note: str, magazine: str) -> bool:
    available = [0] * 26
    base = ord("a")

    for character in magazine:
        available[ord(character) - base] += 1

    for character in ransom_note:
        index = ord(character) - base
        if available[index] == 0:
            return False
        available[index] -= 1

    return True
