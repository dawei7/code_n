from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        row_prefix = [[0] * (columns + 1) for _ in range(rows)]
        column_prefix = [[0] * columns for _ in range(rows + 1)]
        down_right = [[0] * (columns + 1) for _ in range(rows + 1)]
        down_left = [[0] * (columns + 1) for _ in range(rows + 1)]

        for row in range(rows):
            for column in range(columns):
                value = grid[row][column]
                row_prefix[row][column + 1] = row_prefix[row][column] + value
                column_prefix[row + 1][column] = column_prefix[row][column] + value
                down_right[row + 1][column + 1] = down_right[row][column] + value
                down_left[row + 1][column] = down_left[row][column + 1] + value

        for side in range(min(rows, columns), 1, -1):
            for top in range(rows - side + 1):
                bottom = top + side
                for left in range(columns - side + 1):
                    right = left + side
                    target = down_right[bottom][right] - down_right[top][left]
                    other_diagonal = down_left[bottom][left] - down_left[top][right]
                    if other_diagonal != target:
                        continue

                    if any(
                        row_prefix[row][right] - row_prefix[row][left] != target
                        for row in range(top, bottom)
                    ):
                        continue
                    if any(
                        column_prefix[bottom][column] - column_prefix[top][column] != target
                        for column in range(left, right)
                    ):
                        continue
                    return side

        return 1
