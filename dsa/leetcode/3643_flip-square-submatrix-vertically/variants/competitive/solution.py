from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for offset in range(k // 2):
            top = x + offset
            bottom = x + k - 1 - offset
            for column in range(y, y + k):
                grid[top][column], grid[bottom][column] = (
                    grid[bottom][column],
                    grid[top][column],
                )
        return grid
