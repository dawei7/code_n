from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        candidate = 0

        for team in range(1, len(grid)):
            if grid[team][candidate] == 1:
                candidate = team

        return candidate
