from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        row_heaps = [[] for _ in range(rows)]
        column_heaps = [[] for _ in range(columns)]
        unreachable = rows * columns + 1
        distance = unreachable

        for row in range(rows):
            for column in range(columns):
                while row_heaps[row] and row_heaps[row][0][1] < column:
                    heappop(row_heaps[row])
                while column_heaps[column] and column_heaps[column][0][1] < row:
                    heappop(column_heaps[column])

                if row == 0 and column == 0:
                    distance = 1
                else:
                    from_row = row_heaps[row][0][0] if row_heaps[row] else unreachable
                    from_column = (
                        column_heaps[column][0][0]
                        if column_heaps[column]
                        else unreachable
                    )
                    distance = min(from_row, from_column) + 1

                if distance <= rows * columns:
                    heappush(
                        row_heaps[row],
                        (distance, column + grid[row][column]),
                    )
                    heappush(
                        column_heaps[column],
                        (distance, row + grid[row][column]),
                    )

        return distance if distance <= rows * columns else -1
