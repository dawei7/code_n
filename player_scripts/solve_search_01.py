"""Solution for search_01: Linear Search."""

from code_n.api import TrackedList


def solve(data: TrackedList, target: int) -> int:
    """Linear search - O(n)."""
    n = len(data)
    for i in range(n):
        if data.compare_value(i, target) == 0:
            return i
    return -1
