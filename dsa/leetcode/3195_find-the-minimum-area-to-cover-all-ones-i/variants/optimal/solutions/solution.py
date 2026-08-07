class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top, bottom = len(grid), -1
        left, right = len(grid[0]), -1

        for row, values in enumerate(grid):
            for column, value in enumerate(values):
                if value:
                    top = min(top, row)
                    bottom = max(bottom, row)
                    left = min(left, column)
                    right = max(right, column)

        return (bottom - top + 1) * (right - left + 1)
