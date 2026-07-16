from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []
        for row in grid:
            zeros = 0
            for value in reversed(row):
                if value == 1:
                    break
                zeros += 1
            trailing_zeros.append(zeros)

        swaps = 0
        for position in range(n):
            required = n - position - 1
            candidate = position
            while candidate < n and trailing_zeros[candidate] < required:
                candidate += 1
            if candidate == n:
                return -1
            swaps += candidate - position
            trailing_zeros[position + 1:candidate + 1] = trailing_zeros[position:candidate]
            trailing_zeros[position] = required
        return swaps
