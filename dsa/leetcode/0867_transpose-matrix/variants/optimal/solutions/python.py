"""Optimal app-local solution for LeetCode 867."""


def solve(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])
    return [
        [matrix[row][column] for row in range(row_count)]
        for column in range(column_count)
    ]
