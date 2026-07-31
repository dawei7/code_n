import sys


def solve(grid: list[list[int]]) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    sys.setrecursionlimit(rows + cols + 10)

    def find_path(row: int, col: int) -> bool:
        if row >= rows or col >= cols or grid[row][col] == 0:
            return False
        if row == rows - 1 and col == cols - 1:
            return True

        grid[row][col] = 0
        return find_path(row + 1, col) or find_path(row, col + 1)

    if not find_path(0, 0):
        return True

    grid[0][0] = 1
    grid[rows - 1][cols - 1] = 1
    return not find_path(0, 0)
