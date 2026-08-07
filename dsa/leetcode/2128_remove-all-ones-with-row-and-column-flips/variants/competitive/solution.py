from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        first = grid[0]
        for row in grid[1:]:
            should_match = row[0] == first[0]
            for column in range(1, len(first)):
                if (row[column] == first[column]) != should_match:
                    return False
        return True
