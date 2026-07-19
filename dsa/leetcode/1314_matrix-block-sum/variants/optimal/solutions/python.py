"""Optimal app-local solution for LeetCode 1314."""


def solve(mat, k):
    rows = len(mat)
    columns = len(mat[0])
    prefix = [[0] * (columns + 1) for _ in range(rows + 1)]

    for row in range(rows):
        for column in range(columns):
            prefix[row + 1][column + 1] = (
                mat[row][column]
                + prefix[row][column + 1]
                + prefix[row + 1][column]
                - prefix[row][column]
            )

    answer = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        top = max(0, row - k)
        bottom = min(rows, row + k + 1)
        for column in range(columns):
            left = max(0, column - k)
            right = min(columns, column + k + 1)
            answer[row][column] = (
                prefix[bottom][right]
                - prefix[top][right]
                - prefix[bottom][left]
                + prefix[top][left]
            )

    return answer
