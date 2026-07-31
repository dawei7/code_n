def solve(grid: list[list[int]]) -> int:
    row_maxima = [max(row) for row in grid]
    column_maxima = [max(grid[row][col] for row in range(len(grid))) for col in range(len(grid))]

    increase = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            increase += min(row_maxima[row], column_maxima[col]) - grid[row][col]
    return increase
