from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        columns = [0] * n
        for row, column in indices:
            rows[row] ^= 1
            columns[column] ^= 1
        odd_rows = sum(rows)
        odd_columns = sum(columns)
        return odd_rows * (n - odd_columns) + (m - odd_rows) * odd_columns
