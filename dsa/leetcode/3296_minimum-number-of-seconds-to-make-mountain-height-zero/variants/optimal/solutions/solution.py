from math import isqrt
from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            middle = (left + right) // 2
            removed = 0
            for worker_time in workerTimes:
                budget = middle // worker_time
                removed += (isqrt(1 + 8 * budget) - 1) // 2
                if removed >= mountainHeight:
                    break

            if removed >= mountainHeight:
                right = middle
            else:
                left = middle + 1

        return left
