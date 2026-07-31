from math import isqrt
from typing import List


class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        modulo = 1_000_000_007
        width = len(grid[0])

        def spread(values: List[int], row: str, radius: int) -> List[int]:
            prefix = [0] * (width + 1)
            for column, value in enumerate(values):
                prefix[column + 1] = (prefix[column] + value) % modulo
            return [
                (
                    prefix[min(width, column + radius + 1)]
                    - prefix[max(0, column - radius)]
                )
                % modulo
                if cell == "."
                else 0
                for column, cell in enumerate(row)
            ]

        entered = [int(cell == ".") for cell in grid[-1]]
        routes = spread(entered, grid[-1], d)
        upward_radius = isqrt(d * d - 1)

        for row in reversed(grid[:-1]):
            entered = spread(routes, row, upward_radius)
            routes = spread(entered, row, d)

        return sum(routes) % modulo
