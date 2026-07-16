"""Optimal app-local solution for LeetCode 1561."""


def solve(piles: list[int]) -> int:
    """Sum every second pile in the sorted upper two-thirds."""
    ordered = sorted(piles)
    return sum(ordered[len(ordered) // 3 :: 2])
