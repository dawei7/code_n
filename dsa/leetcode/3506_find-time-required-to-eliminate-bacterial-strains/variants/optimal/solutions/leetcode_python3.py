import heapq
from typing import List


class Solution:
    def minEliminationTime(self, timeReq: List[int], splitTime: int) -> int:
        completion_times = timeReq[:]
        heapq.heapify(completion_times)

        while len(completion_times) > 1:
            heapq.heappop(completion_times)
            slower = heapq.heappop(completion_times)
            heapq.heappush(completion_times, slower + splitTime)

        return completion_times[0]
