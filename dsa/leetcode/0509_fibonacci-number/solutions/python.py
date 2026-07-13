"""Constant-space Fibonacci iteration for LeetCode 509."""


def solve(n: int) -> int:
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous
