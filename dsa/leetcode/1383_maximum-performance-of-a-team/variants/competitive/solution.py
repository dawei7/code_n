from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPerformance(
        self,
        n: int,
        speed: List[int],
        efficiency: List[int],
        k: int,
    ) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        speed_sum = 0
        best = 0

        for engineer_efficiency, engineer_speed in engineers:
            heappush(speed_heap, engineer_speed)
            speed_sum += engineer_speed
            if len(speed_heap) > k:
                speed_sum -= heappop(speed_heap)
            best = max(best, speed_sum * engineer_efficiency)

        return best % 1_000_000_007
