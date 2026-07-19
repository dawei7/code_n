from typing import List


# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation.
# class BinaryMatrix(object):
#     def get(self, row: int, col: int) -> int:
#     def dimensions(self) -> List[int]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        row = 0
        col = cols - 1
        answer = -1
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                answer = col
                col -= 1
            else:
                row += 1
        return answer
