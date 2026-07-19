from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        result = [row[:] for row in grid]

        for layer in range(min(rows, columns) // 2):
            top = left = layer
            bottom = rows - 1 - layer
            right = columns - 1 - layer

            coordinates = []
            coordinates.extend((row, left) for row in range(top, bottom + 1))
            coordinates.extend((bottom, column) for column in range(left + 1, right + 1))
            coordinates.extend((row, right) for row in range(bottom - 1, top - 1, -1))
            coordinates.extend((top, column) for column in range(right - 1, left, -1))

            shift = k % len(coordinates)
            for index, (row, column) in enumerate(coordinates):
                target_row, target_column = coordinates[(index + shift) % len(coordinates)]
                result[target_row][target_column] = grid[row][column]

        return result
