"""Optimal solution for dc_14: Staircase Search in Sorted 2D Matrix.

Given an n x m matrix where each row and each
"""


def solve(matrix, n, m, target):
    """Staircase search from the top-right corner."""
    if n == 0 or m == 0:
        return False
    i, j = 0, m - 1
    while i < n and j >= 0:
        v = matrix[i][j]
        if v == target:
            return True
        if v > target:
            j -= 1
        else:
            i += 1
    return False
