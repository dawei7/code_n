"""Optimal solution for dp_02: Climbing Stairs.

Count the number of ways to climb n stairs taking 1 or 2 steps
at a time. Same recurrence as Fibonacci: ways(n) = ways(n-1) +
ways(n-2). O(n) time, O(1) space.
"""


def solve(n):
    if n <= 2:
        return max(n, 1)
    previous, current = 1, 2
    for _ in range(3, n + 1):
        previous, current = current, previous + current
    return current
