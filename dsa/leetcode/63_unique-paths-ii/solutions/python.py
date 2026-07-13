def solve(obstacle_grid: list[list[int]]) -> int:
    paths = [0] * len(obstacle_grid[0])
    paths[0] = 1
    for row in obstacle_grid:
        for column, blocked in enumerate(row):
            if blocked:
                paths[column] = 0
            elif column > 0:
                paths[column] += paths[column - 1]
    return paths[-1]
