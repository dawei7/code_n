from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        size = len(grid)

        for row in range(size):
            for column in range(size):
                on_diagonal = row == column or row + column == size - 1
                if on_diagonal == (grid[row][column] == 0):
                    return False

        return True
