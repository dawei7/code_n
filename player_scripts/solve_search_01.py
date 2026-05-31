"""Solution for search_01: Linear Search."""


def solve(data, target: int) -> int:
    """Linear search - O(n)."""
    n = len(data)
    for index in range(n):
        if data[index] == target:
            return index
    return -1
