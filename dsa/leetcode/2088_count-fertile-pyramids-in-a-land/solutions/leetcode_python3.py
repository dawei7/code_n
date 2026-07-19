from typing import List


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def count_orientation(row_order: range) -> int:
            supporting = [0] * columns
            total = 0

            for row in row_order:
                current = [0] * columns
                for column in range(columns):
                    if grid[row][column] == 0:
                        continue
                    current[column] = 1
                    if 0 < column < columns - 1:
                        current[column] += min(
                            supporting[column - 1],
                            supporting[column],
                            supporting[column + 1],
                        )
                    total += current[column] - 1
                supporting = current

            return total

        return count_orientation(range(rows - 1, -1, -1)) + count_orientation(
            range(rows)
        )
