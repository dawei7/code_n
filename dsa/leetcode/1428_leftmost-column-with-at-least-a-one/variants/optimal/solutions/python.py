"""Optimal app-local solution for LeetCode 1428."""


def solve(binary_matrix) -> int:
    rows, cols = binary_matrix.dimensions()
    row = 0
    col = cols - 1
    answer = -1
    while row < rows and col >= 0:
        if binary_matrix.get(row, col) == 1:
            answer = col
            col -= 1
        else:
            row += 1
    return answer
