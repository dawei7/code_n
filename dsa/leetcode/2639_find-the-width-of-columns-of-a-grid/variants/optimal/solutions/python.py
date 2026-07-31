def solve(grid: list[list[int]]) -> list[int]:
    return [
        max(len(str(row[column])) for row in grid)
        for column in range(len(grid[0]))
    ]
