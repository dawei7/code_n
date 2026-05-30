"""Example solution for search_02: Binary Search.

Find a target value in a sorted TrackedList.

Run with:
    python run_challenge.py search_02 player_scripts/solve_search_02.py
"""

from code_n.api import TrackedList


def solve(data: TrackedList, target: int, n: int) -> int:
    """Binary search - O(log n) solution."""
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        cmp = data.compare_value(mid, target)  # 1 comparison

        if cmp == 0:
            return mid
        elif cmp < 0:
            low = mid + 1
        else:
            high = mid - 1

    return -1
