"""Simplified app-local solution for LeetCode 1502."""


def solve(arr: list[int]) -> bool:
    """Return whether all values can be reordered into a progression."""
    ordered = sorted(arr)
    difference = ordered[1] - ordered[0]
    return all(
        ordered[index] - ordered[index - 1] == difference
        for index in range(2, len(ordered))
    )
