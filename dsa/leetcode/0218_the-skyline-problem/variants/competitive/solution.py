import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted({b[0] for b in buildings} | {b[1] for b in buildings})
        active = [(0, float("inf"))]
        result = []
        index = 0
        for x in events:
            while index < len(buildings) and buildings[index][0] == x:
                _, right, height = buildings[index]
                heapq.heappush(active, (-height, right))
                index += 1
            while active[0][1] <= x:
                heapq.heappop(active)
            height = -active[0][0]
            if not result or result[-1][1] != height:
                result.append([x, height])
        return result
