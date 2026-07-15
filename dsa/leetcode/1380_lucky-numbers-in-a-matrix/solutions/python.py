"""Reference solution for LeetCode 1380."""


def solve(matrix: list[list[int]]) -> list[int]:
    rows = len(matrix)
    columns = len(matrix[0])
    column_maxima = [
        max(matrix[row][column] for row in range(rows))
        for column in range(columns)
    ]

    lucky = []
    for row in matrix:
        minimum_column = min(range(columns), key=row.__getitem__)
        if row[minimum_column] == column_maxima[minimum_column]:
            lucky.append(row[minimum_column])

    return lucky
