from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        remaining = 0
        farthest_right = -1
        for _, right in intervals:
            if right > farthest_right:
                remaining += 1
                farthest_right = right
        return remaining
