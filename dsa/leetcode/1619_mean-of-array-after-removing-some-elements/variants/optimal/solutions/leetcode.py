from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        ordered = sorted(arr)
        trim = len(arr) // 20
        middle = ordered[trim : len(arr) - trim]
        return sum(middle) / len(middle)
