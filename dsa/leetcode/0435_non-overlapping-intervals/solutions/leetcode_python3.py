from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        kept = 0
        previous_end = float("-inf")
        for start, end in sorted(intervals, key=lambda interval: interval[1]):
            if start >= previous_end:
                kept += 1
                previous_end = end
        return len(intervals) - kept
