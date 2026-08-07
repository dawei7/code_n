from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, rows * columns - 1
        while left <= right:
            middle = (left + right) // 2
            value = matrix[middle // columns][middle % columns]
            if value == target:
                return True
            if value < target:
                left = middle + 1
            else:
                right = middle - 1
        return False
