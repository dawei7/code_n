def solve(grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
    for offset in range(k // 2):
        top = x + offset
        bottom = x + k - 1 - offset
        for column in range(y, y + k):
            grid[top][column], grid[bottom][column] = (
                grid[bottom][column],
                grid[top][column],
            )
    return grid
