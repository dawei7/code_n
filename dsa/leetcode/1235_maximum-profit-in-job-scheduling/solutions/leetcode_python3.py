from bisect import bisect_left
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [start for start, _, _ in jobs]
        best = [0] * (len(jobs) + 1)

        for index in range(len(jobs) - 1, -1, -1):
            _, end, gain = jobs[index]
            next_index = bisect_left(starts, end, index + 1)
            best[index] = max(best[index + 1], gain + best[next_index])

        return best[0]
