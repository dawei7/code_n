from functools import lru_cache


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        row_prefix = [[0] * (columns + 1) for _ in range(rows)]
        column_prefix = [[0] * (rows + 1) for _ in range(columns)]
        for row in range(rows):
            for column in range(columns):
                row_prefix[row][column + 1] = row_prefix[row][column] + grid[row][column]
        for column in range(columns):
            for row in range(rows):
                column_prefix[column][row + 1] = (
                    column_prefix[column][row] + grid[row][column]
                )

        @lru_cache(maxsize=None)
        def area(top: int, bottom: int, left: int, right: int) -> int:
            first_row = last_row = first_column = last_column = -1

            for row in range(top, bottom + 1):
                if row_prefix[row][right + 1] - row_prefix[row][left]:
                    first_row = row
                    break
            if first_row == -1:
                return 0
            for row in range(bottom, top - 1, -1):
                if row_prefix[row][right + 1] - row_prefix[row][left]:
                    last_row = row
                    break
            for column in range(left, right + 1):
                if column_prefix[column][bottom + 1] - column_prefix[column][top]:
                    first_column = column
                    break
            for column in range(right, left - 1, -1):
                if column_prefix[column][bottom + 1] - column_prefix[column][top]:
                    last_column = column
                    break

            return (last_row - first_row + 1) * (last_column - first_column + 1)

        answer = float("inf")

        for first in range(rows - 2):
            for second in range(first + 1, rows - 1):
                answer = min(
                    answer,
                    area(0, first, 0, columns - 1)
                    + area(first + 1, second, 0, columns - 1)
                    + area(second + 1, rows - 1, 0, columns - 1),
                )

        for first in range(columns - 2):
            for second in range(first + 1, columns - 1):
                answer = min(
                    answer,
                    area(0, rows - 1, 0, first)
                    + area(0, rows - 1, first + 1, second)
                    + area(0, rows - 1, second + 1, columns - 1),
                )

        for row_cut in range(rows - 1):
            for column_cut in range(columns - 1):
                answer = min(
                    answer,
                    area(0, row_cut, 0, column_cut)
                    + area(0, row_cut, column_cut + 1, columns - 1)
                    + area(row_cut + 1, rows - 1, 0, columns - 1),
                    area(0, row_cut, 0, columns - 1)
                    + area(row_cut + 1, rows - 1, 0, column_cut)
                    + area(row_cut + 1, rows - 1, column_cut + 1, columns - 1),
                    area(0, rows - 1, 0, column_cut)
                    + area(0, row_cut, column_cut + 1, columns - 1)
                    + area(row_cut + 1, rows - 1, column_cut + 1, columns - 1),
                    area(0, row_cut, 0, column_cut)
                    + area(row_cut + 1, rows - 1, 0, column_cut)
                    + area(0, rows - 1, column_cut + 1, columns - 1),
                )

        return int(answer)
