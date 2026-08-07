from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        required = set(range(1, n + 1))
        for index in range(n):
            if set(matrix[index]) != required:
                return False
            if {matrix[row][index] for row in range(n)} != required:
                return False
        return True
