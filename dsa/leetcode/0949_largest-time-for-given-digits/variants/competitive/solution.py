from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1
        for first, second, third, fourth in permutations(arr):
            hour = first * 10 + second
            minute = third * 10 + fourth
            if hour < 24 and minute < 60:
                best = max(best, hour * 60 + minute)

        if best < 0:
            return ""
        return f"{best // 60:02d}:{best % 60:02d}"
