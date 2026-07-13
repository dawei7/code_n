from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = [0] * len(obstacleGrid[0])
        paths[0] = 1
        for row in obstacleGrid:
            for column, blocked in enumerate(row):
                if blocked:
                    paths[column] = 0
                elif column > 0:
                    paths[column] += paths[column - 1]
        return paths[-1]
