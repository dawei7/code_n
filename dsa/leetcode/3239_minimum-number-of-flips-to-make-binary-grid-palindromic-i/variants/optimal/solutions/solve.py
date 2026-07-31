def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])

    row_mismatches = sum(
        grid[row][left] != grid[row][columns - 1 - left] for row in range(rows) for left in range(columns // 2)
    )
    column_mismatches = sum(
        grid[top][column] != grid[rows - 1 - top][column] for top in range(rows // 2) for column in range(columns)
    )
    return min(row_mismatches, column_mismatches)
