"""Example solution for sort_01: Bubble Sort.

Sort a TrackedList using only adjacent compare and swap.

Run with:
    python run_challenge.py sort_01 player_scripts/solve_sort_01.py
"""

from code_n.api import TrackedList


def solve(data: TrackedList, n: int) -> TrackedList:
    """Bubble sort - O(n²) solution."""
    for i in range(n):
        for j in range(0, n - i - 1):
            if data.compare(j, j + 1) > 0:  # 1 comparison
                data.swap(j, j + 1)          # 1 swap
    return data
