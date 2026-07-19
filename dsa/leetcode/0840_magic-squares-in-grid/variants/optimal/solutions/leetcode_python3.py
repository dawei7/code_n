from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        magic_values = set(range(1, 10))

        def is_magic(top: int, left: int) -> bool:
            if grid[top + 1][left + 1] != 5:
                return False

            values = {
                grid[top + row_offset][left + column_offset]
                for row_offset in range(3)
                for column_offset in range(3)
            }
            if values != magic_values:
                return False

            for offset in range(3):
                if sum(grid[top + offset][left : left + 3]) != 15:
                    return False
                if sum(grid[top + row][left + offset] for row in range(3)) != 15:
                    return False

            return (
                sum(grid[top + offset][left + offset] for offset in range(3)) == 15
                and sum(grid[top + offset][left + 2 - offset] for offset in range(3)) == 15
            )

        return sum(
            is_magic(top, left)
            for top in range(rows - 2)
            for left in range(columns - 2)
        )
