from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        minimum = [[0] * columns for _ in range(rows)]
        maximum = [[0] * columns for _ in range(rows)]
        minimum[0][0] = maximum[0][0] = grid[0][0]

        for row in range(rows):
            for column in range(columns):
                if row == 0 and column == 0:
                    continue

                value = grid[row][column]
                candidates = []
                if row > 0:
                    candidates.append(minimum[row - 1][column] * value)
                    candidates.append(maximum[row - 1][column] * value)
                if column > 0:
                    candidates.append(minimum[row][column - 1] * value)
                    candidates.append(maximum[row][column - 1] * value)
                minimum[row][column] = min(candidates)
                maximum[row][column] = max(candidates)

        answer = maximum[-1][-1]
        return answer % 1_000_000_007 if answer >= 0 else -1
