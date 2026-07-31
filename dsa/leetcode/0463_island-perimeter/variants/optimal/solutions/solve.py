"""Shared-edge counting solution for LeetCode 463."""


def solve(grid: list[list[int]]) -> int:
    perimeter = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 0:
                continue
            perimeter += 4
            if row > 0 and grid[row - 1][column] == 1:
                perimeter -= 2
            if column > 0 and grid[row][column - 1] == 1:
                perimeter -= 2
    return perimeter
