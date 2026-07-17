from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        columns = len(grid[0])
        answer = []

        for start in range(columns):
            column = start
            for row in grid:
                next_column = column + row[column]
                if (
                    next_column < 0
                    or next_column >= columns
                    or row[next_column] != row[column]
                ):
                    column = -1
                    break
                column = next_column
            answer.append(column)

        return answer
