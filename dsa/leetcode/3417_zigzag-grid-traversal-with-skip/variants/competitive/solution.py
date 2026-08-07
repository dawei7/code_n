from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        result = []
        take = True

        for row, values in enumerate(grid):
            if row % 2 == 0:
                columns = range(len(values))
            else:
                columns = range(len(values) - 1, -1, -1)

            for column in columns:
                if take:
                    result.append(values[column])
                take = not take

        return result
