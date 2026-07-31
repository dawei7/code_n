def solve(grid: list[list[int]]) -> bool:
    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if row + 1 < rows and grid[row][column] != grid[row + 1][column]:
                return False
            if column + 1 < columns and grid[row][column] == grid[row][column + 1]:
                return False

    return True
