"""Deliberately BAD solution for search_02: uses linear search on sorted data.

This should FAIL the complexity check (O(n) instead of required O(log n)).
"""


def solve(data, target: int, n: int) -> int:
    """Linear search - O(n) - will FAIL the O(log n) requirement!"""
    for index in range(n):
        if data[index] == target:
            return index
    return -1
