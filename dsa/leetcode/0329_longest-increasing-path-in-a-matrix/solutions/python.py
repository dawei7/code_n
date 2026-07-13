from collections import deque


def _longest_increasing_path(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    outdegree = [[0] * columns for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and matrix[next_row][next_column] > matrix[row][column]
                ):
                    outdegree[row][column] += 1

    queue = deque(
        (row, column)
        for row in range(rows)
        for column in range(columns)
        if outdegree[row][column] == 0
    )
    layers = 0
    while queue:
        layers += 1
        for _ in range(len(queue)):
            row, column = queue.popleft()
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and matrix[next_row][next_column] < matrix[row][column]
                ):
                    outdegree[next_row][next_column] -= 1
                    if outdegree[next_row][next_column] == 0:
                        queue.append((next_row, next_column))
    return layers


def solve(matrix: list[list[int]]) -> int:
    return _longest_increasing_path(matrix)
