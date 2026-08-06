"""Proposed app-local solution for LeetCode 1165."""


def solve(keyboard: str, word: str) -> int:
    positions = {character: position for position, character in enumerate(keyboard)}
    current = 0
    total = 0
    for character in word:
        destination = positions[character]
        total += abs(destination - current)
        current = destination
    return total
