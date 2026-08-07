from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        columns = len(grid[0])
        column_balance = [0] * columns
        column_x_count = [0] * columns
        answer = 0

        for row in grid:
            prefix_balance = 0
            prefix_x_count = 0
            for column, value in enumerate(row):
                if value == "X":
                    column_balance[column] += 1
                    column_x_count[column] += 1
                elif value == "Y":
                    column_balance[column] -= 1

                prefix_balance += column_balance[column]
                prefix_x_count += column_x_count[column]
                if prefix_balance == 0 and prefix_x_count > 0:
                    answer += 1

        return answer
