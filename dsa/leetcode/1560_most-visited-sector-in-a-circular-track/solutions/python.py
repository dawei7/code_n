"""Optimal app-local solution for LeetCode 1560."""


def solve(n: int, rounds: list[int]) -> list[int]:
    """Return the inclusive clockwise endpoint arc in sorted order."""
    start = rounds[0]
    end = rounds[-1]
    if start <= end:
        return list(range(start, end + 1))
    return list(range(1, end + 1)) + list(range(start, n + 1))
