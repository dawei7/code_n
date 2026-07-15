from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        column_maxima = [0] * len(grid)
        top_area = 0
        row_area = 0

        for row in grid:
            row_area += max(row)
            for column, height in enumerate(row):
                if height > 0:
                    top_area += 1
                if height > column_maxima[column]:
                    column_maxima[column] = height

        return top_area + row_area + sum(column_maxima)
