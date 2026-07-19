from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        best = 0
        for sign1, sign2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            low = float("inf")
            high = float("-inf")
            for index, (value1, value2) in enumerate(zip(arr1, arr2)):
                transformed = sign1 * value1 + sign2 * value2 + index
                low = min(low, transformed)
                high = max(high, transformed)
            best = max(best, high - low)
        return best
