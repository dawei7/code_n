"""Optimal app-local solution for LeetCode 1165."""


def solve(keyboard: str, word: str) -> int:
    positions = {character: index for index, character in enumerate(keyboard)}
    current = 0
    total = 0
    for character in word:
        destination = positions[character]
        total += abs(destination - current)
        current = destination
    return total
