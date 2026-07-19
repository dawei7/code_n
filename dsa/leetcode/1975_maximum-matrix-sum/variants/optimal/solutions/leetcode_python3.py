from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negative_count = 0
        smallest = float("inf")

        for row in matrix:
            for value in row:
                magnitude = abs(value)
                total += magnitude
                smallest = min(smallest, magnitude)
                negative_count += value < 0

        if negative_count % 2:
            total -= 2 * smallest
        return int(total)
