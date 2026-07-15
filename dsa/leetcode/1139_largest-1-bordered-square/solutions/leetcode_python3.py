from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        right = [[0] * columns for _ in range(rows)]
        down = [[0] * columns for _ in range(rows)]

        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                if grid[row][column] == 1:
                    right[row][column] = 1 + (right[row][column + 1] if column + 1 < columns else 0)
                    down[row][column] = 1 + (down[row + 1][column] if row + 1 < rows else 0)

        for side in range(min(rows, columns), 0, -1):
            for row in range(rows - side + 1):
                bottom = row + side - 1
                for column in range(columns - side + 1):
                    far_right = column + side - 1
                    if (
                        right[row][column] >= side
                        and down[row][column] >= side
                        and right[bottom][column] >= side
                        and down[row][far_right] >= side
                    ):
                        return side * side
        return 0
