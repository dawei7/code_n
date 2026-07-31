"""Optimal app-local solution for LeetCode 1134."""


def solve(n: int) -> bool:
    digits = 0
    remaining = n
    while remaining:
        digits += 1
        remaining //= 10

    total = 0
    remaining = n
    while remaining:
        digit = remaining % 10
        total += digit**digits
        remaining //= 10
    return total == n
