from heapq import heappop, heappush
from typing import List


class Solution:
    def furthestBuilding(
        self, heights: List[int], bricks: int, ladders: int
    ) -> int:
        ladder_climbs: List[int] = []

        for index in range(len(heights) - 1):
            climb = heights[index + 1] - heights[index]
            if climb <= 0:
                continue
            heappush(ladder_climbs, climb)
            if len(ladder_climbs) > ladders:
                bricks -= heappop(ladder_climbs)
                if bricks < 0:
                    return index

        return len(heights) - 1
