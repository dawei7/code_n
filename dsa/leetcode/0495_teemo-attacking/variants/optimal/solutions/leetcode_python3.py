from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = duration
        for index in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[index + 1] - timeSeries[index])
        return total
