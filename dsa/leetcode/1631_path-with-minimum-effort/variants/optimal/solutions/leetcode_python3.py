import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])
        efforts = [[float("inf")] * columns for _ in range(rows)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            effort, row, column = heapq.heappop(heap)
            if (row, column) == (rows - 1, columns - 1):
                return effort
            if effort != efforts[row][column]:
                continue
            for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_step
                next_column = column + column_step
                if not (0 <= next_row < rows and 0 <= next_column < columns):
                    continue
                edge = abs(heights[row][column] - heights[next_row][next_column])
                next_effort = max(effort, edge)
                if next_effort < efforts[next_row][next_column]:
                    efforts[next_row][next_column] = next_effort
                    heapq.heappush(heap, (next_effort, next_row, next_column))
        return 0
