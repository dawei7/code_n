def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    answer = 0

    for row in range(rows - 2):
        for column in range(columns - 2):
            current = (
                grid[row][column]
                + grid[row][column + 1]
                + grid[row][column + 2]
                + grid[row + 1][column + 1]
                + grid[row + 2][column]
                + grid[row + 2][column + 1]
                + grid[row + 2][column + 2]
            )
            answer = max(answer, current)

    return answer
