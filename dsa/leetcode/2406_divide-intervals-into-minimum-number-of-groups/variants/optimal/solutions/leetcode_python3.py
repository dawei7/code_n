from heapq import heappop, heappush
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        active_ends = []
        maximum_overlap = 0

        for left, right in sorted(intervals):
            while active_ends and active_ends[0] < left:
                heappop(active_ends)
            heappush(active_ends, right)
            maximum_overlap = max(maximum_overlap, len(active_ends))

        return maximum_overlap
