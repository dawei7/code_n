"""Optimal app-local solution for LeetCode 931."""


def solve(matrix):
    previous = matrix[0][:]
    size = len(matrix)
    for row in range(1, size):
        current = [0] * size
        for column in range(size):
            left = max(0, column - 1)
            right = min(size, column + 2)
            current[column] = matrix[row][column] + min(previous[left:right])
        previous = current
    return min(previous)
