from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        row_twos = [[0] * (columns + 1) for _ in range(rows)]
        row_fives = [[0] * (columns + 1) for _ in range(rows)]
        column_twos = [[0] * columns for _ in range(rows + 1)]
        column_fives = [[0] * columns for _ in range(rows + 1)]
        factors = [[(0, 0)] * columns for _ in range(rows)]

        for row in range(rows):
            for column in range(columns):
                value = grid[row][column]
                twos = fives = 0
                while value % 2 == 0:
                    twos += 1
                    value //= 2
                while value % 5 == 0:
                    fives += 1
                    value //= 5
                factors[row][column] = (twos, fives)
                row_twos[row][column + 1] = row_twos[row][column] + twos
                row_fives[row][column + 1] = row_fives[row][column] + fives
                column_twos[row + 1][column] = column_twos[row][column] + twos
                column_fives[row + 1][column] = column_fives[row][column] + fives

        answer = 0
        for row in range(rows):
            for column in range(columns):
                cell_twos, cell_fives = factors[row][column]
                horizontal_twos = (
                    row_twos[row][column + 1],
                    row_twos[row][columns] - row_twos[row][column],
                )
                horizontal_fives = (
                    row_fives[row][column + 1],
                    row_fives[row][columns] - row_fives[row][column],
                )
                vertical_twos = (
                    column_twos[row + 1][column],
                    column_twos[rows][column] - column_twos[row][column],
                )
                vertical_fives = (
                    column_fives[row + 1][column],
                    column_fives[rows][column] - column_fives[row][column],
                )
                for horizontal in range(2):
                    for vertical in range(2):
                        twos = horizontal_twos[horizontal] + vertical_twos[vertical] - cell_twos
                        fives = horizontal_fives[horizontal] + vertical_fives[vertical] - cell_fives
                        answer = max(answer, min(twos, fives))
        return answer
