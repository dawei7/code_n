"""Optimal app-local solution for LeetCode 892."""


def solve(grid):
    area = 0
    for row in range(len(grid)):
        for column in range(len(grid)):
            height = grid[row][column]
            if height == 0:
                continue
            area += 4 * height + 2
            if row > 0:
                area -= 2 * min(height, grid[row - 1][column])
            if column > 0:
                area -= 2 * min(height, grid[row][column - 1])
    return area
