from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for row in range(size):
            for column in range(row + 1, size):
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column],
                )
        for row in matrix:
            row.reverse()
