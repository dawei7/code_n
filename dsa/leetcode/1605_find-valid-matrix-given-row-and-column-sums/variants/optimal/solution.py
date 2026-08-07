from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in rowSum]
        row = column = 0

        while row < len(rowSum) and column < len(colSum):
            value = min(rowSum[row], colSum[column])
            matrix[row][column] = value
            rowSum[row] -= value
            colSum[column] -= value
            if rowSum[row] == 0:
                row += 1
            if colSum[column] == 0:
                column += 1

        return matrix
