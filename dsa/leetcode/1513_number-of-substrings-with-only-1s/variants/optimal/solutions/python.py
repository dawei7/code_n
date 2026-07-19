"""Optimal app-local solution for LeetCode 1513."""


def solve(s: str) -> int:
    """Count all-one substrings by their right endpoints."""
    modulo = 1_000_000_007
    run = 0
    total = 0
    for character in s:
        if character == "1":
            run += 1
            total = (total + run) % modulo
        else:
            run = 0
    return total
