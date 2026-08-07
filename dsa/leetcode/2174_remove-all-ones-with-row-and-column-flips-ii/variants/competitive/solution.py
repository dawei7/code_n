from functools import cache
from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        cell_count = rows * columns
        initial_mask = 0
        clear_masks = [0] * cell_count

        for row in range(rows):
            for column in range(columns):
                position = row * columns + column
                if grid[row][column]:
                    initial_mask |= 1 << position

                for other_column in range(columns):
                    clear_masks[position] |= 1 << (row * columns + other_column)
                for other_row in range(rows):
                    clear_masks[position] |= 1 << (other_row * columns + column)

        @cache
        def best(mask: int) -> int:
            if mask == 0:
                return 0
            return 1 + min(
                best(mask & ~clear_masks[position]) for position in range(cell_count) if mask & (1 << position)
            )

        return best(initial_mask)
