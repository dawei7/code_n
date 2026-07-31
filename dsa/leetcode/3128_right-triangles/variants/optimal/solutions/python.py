def solve(grid: list[list[int]]) -> int:
    row_counts = [sum(row) for row in grid]
    column_counts = [sum(column) for column in zip(*grid)]

    triangles = 0
    for row, values in enumerate(grid):
        for column, value in enumerate(values):
            if value:
                triangles += (row_counts[row] - 1) * (column_counts[column] - 1)
    return triangles
