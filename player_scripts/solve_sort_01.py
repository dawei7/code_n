"""Example solution for sort_01: Bubble Sort.

Sort the list-like data with normal Python indexing and assignment.

Run with:
    python run_challenge.py sort_01 player_scripts/solve_sort_01.py
"""


def solve(data, n):
    """Bubble sort - O(n²) solution."""
    for end in range(n - 1, 0, -1):
        for index in range(end):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
    return data
