from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        total = rows * columns
        k %= total
        flat = [value for row in grid for value in row]
        shifted = flat[-k:] + flat[:-k] if k else flat
        return [shifted[index:index + columns] for index in range(0, total, columns)]
