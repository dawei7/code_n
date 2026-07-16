"""Optimal app-local solution for LeetCode 1502."""


def solve(arr: list[int]) -> bool:
    """Return whether all values can be reordered into a progression."""
    n = len(arr)
    low = min(arr)
    high = max(arr)
    span = high - low

    if span == 0:
        return True
    if span % (n - 1) != 0:
        return False

    difference = span // (n - 1)
    values = set(arr)
    if len(values) != n:
        return False

    return all(low + index * difference in values for index in range(n))
