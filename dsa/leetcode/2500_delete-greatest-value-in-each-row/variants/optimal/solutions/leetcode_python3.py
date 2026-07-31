class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        answer = 0
        for column in range(len(grid[0])):
            answer += max(row[column] for row in grid)
        return answer
