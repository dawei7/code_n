from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        columns = len(isWater[0])
        heights = [[-1] * columns for _ in range(rows)]
        queue = deque()

        for row in range(rows):
            for column in range(columns):
                if isWater[row][column] == 1:
                    heights[row][column] = 0
                    queue.append((row, column))

        while queue:
            row, column = queue.popleft()
            for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_step
                next_column = column + column_step
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and heights[next_row][next_column] == -1
                ):
                    heights[next_row][next_column] = heights[row][column] + 1
                    queue.append((next_row, next_column))

        return heights
