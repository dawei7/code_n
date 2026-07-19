def solve(arr: list[int]) -> int:
    """Return the greatest achievable element after valid transformations."""
    maximum = 0
    for value in sorted(arr):
        maximum = min(value, maximum + 1)
    return maximum
