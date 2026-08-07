from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        available = []
        project_index = 0
        for _ in range(k):
            while project_index < len(projects) and projects[project_index][0] <= w:
                heappush(available, -projects[project_index][1])
                project_index += 1
            if not available:
                break
            w -= heappop(available)
        return w
