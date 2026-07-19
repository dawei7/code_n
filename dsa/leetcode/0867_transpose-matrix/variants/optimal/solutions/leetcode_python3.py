from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_count = len(matrix)
        column_count = len(matrix[0])
        return [
            [matrix[row][column] for row in range(row_count)]
            for column in range(column_count)
        ]
