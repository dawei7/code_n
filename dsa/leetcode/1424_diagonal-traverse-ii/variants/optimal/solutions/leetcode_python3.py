from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = []
        for row, values in enumerate(nums):
            for column, value in enumerate(values):
                diagonal = row + column
                while len(diagonals) <= diagonal:
                    diagonals.append([])
                diagonals[diagonal].append(value)

        traversal = []
        for diagonal in diagonals:
            traversal.extend(reversed(diagonal))
        return traversal
