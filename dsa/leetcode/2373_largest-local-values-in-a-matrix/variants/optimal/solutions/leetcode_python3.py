from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        return [
            [
                max(
                    grid[row + dr][col + dc]
                    for dr in range(3)
                    for dc in range(3)
                )
                for col in range(n - 2)
            ]
            for row in range(n - 2)
        ]
