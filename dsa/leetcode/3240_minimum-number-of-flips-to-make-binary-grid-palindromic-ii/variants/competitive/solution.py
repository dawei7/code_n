from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        flips = 0

        for top in range(rows // 2):
            for left in range(columns // 2):
                ones = (
                    grid[top][left]
                    + grid[top][columns - 1 - left]
                    + grid[rows - 1 - top][left]
                    + grid[rows - 1 - top][columns - 1 - left]
                )
                flips += min(ones, 4 - ones)

        mismatched_pairs = 0
        matched_pair_ones = 0

        if rows % 2:
            middle_row = rows // 2
            for left in range(columns // 2):
                first = grid[middle_row][left]
                second = grid[middle_row][columns - 1 - left]
                if first != second:
                    mismatched_pairs += 1
                else:
                    matched_pair_ones += first + second

        if columns % 2:
            middle_column = columns // 2
            for top in range(rows // 2):
                first = grid[top][middle_column]
                second = grid[rows - 1 - top][middle_column]
                if first != second:
                    mismatched_pairs += 1
                else:
                    matched_pair_ones += first + second

        flips += mismatched_pairs

        if rows % 2 and columns % 2:
            flips += grid[rows // 2][columns // 2]

        if mismatched_pairs == 0 and matched_pair_ones % 4 == 2:
            flips += 2

        return flips
