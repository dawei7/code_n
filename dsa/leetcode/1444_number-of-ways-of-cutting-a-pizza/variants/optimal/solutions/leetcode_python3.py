from functools import lru_cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        modulo = 1_000_000_007
        rows = len(pizza)
        columns = len(pizza[0])

        suffix_apples = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                suffix_apples[row][column] = (
                    int(pizza[row][column] == "A")
                    + suffix_apples[row + 1][column]
                    + suffix_apples[row][column + 1]
                    - suffix_apples[row + 1][column + 1]
                )

        @lru_cache(None)
        def count_ways(row: int, column: int, pieces: int) -> int:
            if suffix_apples[row][column] < pieces:
                return 0
            if pieces == 1:
                return 1

            result = 0
            for next_row in range(row + 1, rows):
                if suffix_apples[row][column] > suffix_apples[next_row][column]:
                    result += count_ways(next_row, column, pieces - 1)

            for next_column in range(column + 1, columns):
                if suffix_apples[row][column] > suffix_apples[row][next_column]:
                    result += count_ways(row, next_column, pieces - 1)

            return result % modulo

        return count_ways(0, 0, k)
