def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    best = -10**18

    for values in grid:
        ending = values[0] + values[1]
        best = max(best, ending)
        for col in range(2, cols):
            ending = max(ending + values[col], values[col - 1] + values[col])
            best = max(best, ending)

    for col in range(cols):
        ending = grid[0][col] + grid[1][col]
        best = max(best, ending)
        for row in range(2, rows):
            ending = max(
                ending + grid[row][col],
                grid[row - 1][col] + grid[row][col],
            )
            best = max(best, ending)

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            best = max(best, grid[row][col])

    return best
