from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, columns = len(grid), len(grid[0])
        down_right = [[0] * (columns + 2) for _ in range(rows + 1)]
        down_left = [[0] * (columns + 2) for _ in range(rows + 1)]

        for row, values in enumerate(grid, 1):
            for column, value in enumerate(values, 1):
                down_right[row][column] = (
                    down_right[row - 1][column - 1] + value
                )
                down_left[row][column] = down_left[row - 1][column + 1] + value

        biggest = set()

        def retain(value: int) -> None:
            biggest.add(value)
            if len(biggest) > 3:
                biggest.remove(min(biggest))

        for row, values in enumerate(grid, 1):
            for column, value in enumerate(values, 1):
                retain(value)
                max_radius = min(
                    row - 1,
                    rows - row,
                    column - 1,
                    columns - column,
                )
                for radius in range(1, max_radius + 1):
                    lower_left = (
                        down_right[row + radius][column]
                        - down_right[row][column - radius]
                    )
                    upper_right = (
                        down_right[row][column + radius]
                        - down_right[row - radius][column]
                    )
                    upper_left = (
                        down_left[row][column - radius]
                        - down_left[row - radius][column]
                    )
                    lower_right = (
                        down_left[row + radius][column]
                        - down_left[row][column + radius]
                    )
                    border_sum = (
                        lower_left
                        + upper_right
                        + upper_left
                        + lower_right
                        - grid[row + radius - 1][column - 1]
                        + grid[row - radius - 1][column - 1]
                    )
                    retain(border_sum)

        return sorted(biggest, reverse=True)
