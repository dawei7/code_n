from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(start + duration for start, duration in tasks)
