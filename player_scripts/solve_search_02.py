"""Example solution for search_02: Binary Search.

Find a target value in a sorted list-like input.

Run with:
    python run_challenge.py search_02 player_scripts/solve_search_02.py
"""


def solve(data, target: int, n: int) -> int:
    """Binary search - O(log n) solution."""
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        value = data[mid]
        if value == target:
            return mid
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
