"""Optimal solution for LeetCode 1074: Number of Submatrices That Sum to Target."""

from collections import Counter


def solve(matrix: list[list[int]], target: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    answer = 0
    for top in range(rows):
        col_sums = [0] * cols
        for bottom in range(top, rows):
            for c in range(cols):
                col_sums[c] += matrix[bottom][c]
            counts = Counter({0: 1})
            running = 0
            for value in col_sums:
                running += value
                answer += counts[running - target]
                counts[running] += 1
    return answer
