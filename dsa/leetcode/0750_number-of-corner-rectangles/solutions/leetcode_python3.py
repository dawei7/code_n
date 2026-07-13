from typing import List


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        if columns > rows:
            grid = [list(column) for column in zip(*grid)]
            rows, columns = columns, rows

        pair_counts = [[0] * columns for _ in range(columns)]
        rectangles = 0

        for row in grid:
            one_columns = [column for column, value in enumerate(row) if value == 1]
            for left_index in range(len(one_columns)):
                left = one_columns[left_index]
                for right_index in range(left_index + 1, len(one_columns)):
                    right = one_columns[right_index]
                    rectangles += pair_counts[left][right]
                    pair_counts[left][right] += 1

        return rectangles
