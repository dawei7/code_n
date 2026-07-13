from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_index in range(numRows):
            row = [1] * (row_index + 1)
            for column in range(1, row_index):
                row[column] = triangle[-1][column - 1] + triangle[-1][column]
            triangle.append(row)
        return triangle
