"""Deliberately BAD solution for search_02: uses linear search on sorted data.

This should FAIL the complexity check (O(n) instead of required O(log n)).
"""

from code_n.api import TrackedList


def solve(data: TrackedList, target: int, n: int) -> int:
    """Linear search - O(n) - will FAIL the O(log n) requirement!"""
    for i in range(n):
        if data.compare_value(i, target) == 0:
            return i
    return -1
