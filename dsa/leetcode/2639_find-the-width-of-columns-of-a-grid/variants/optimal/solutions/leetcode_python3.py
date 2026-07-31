class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [
            max(len(str(row[column])) for row in grid)
            for column in range(len(grid[0]))
        ]
