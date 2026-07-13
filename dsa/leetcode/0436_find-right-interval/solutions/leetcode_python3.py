from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indexed_starts = sorted((start, index) for index, (start, _) in enumerate(intervals))
        starts = [start for start, _ in indexed_starts]
        answer = []
        for _, end in intervals:
            position = bisect_left(starts, end)
            answer.append(-1 if position == len(starts) else indexed_starts[position][1])
        return answer
