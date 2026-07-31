from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        difference = [[0] * n for _ in range(n)]

        for row1, col1, row2, col2 in queries:
            difference[row1][col1] += 1
            if row2 + 1 < n:
                difference[row2 + 1][col1] -= 1
            if col2 + 1 < n:
                difference[row1][col2 + 1] -= 1
            if row2 + 1 < n and col2 + 1 < n:
                difference[row2 + 1][col2 + 1] += 1

        for row in range(n):
            for col in range(n):
                if row:
                    difference[row][col] += difference[row - 1][col]
                if col:
                    difference[row][col] += difference[row][col - 1]
                if row and col:
                    difference[row][col] -= difference[row - 1][col - 1]

        return difference
