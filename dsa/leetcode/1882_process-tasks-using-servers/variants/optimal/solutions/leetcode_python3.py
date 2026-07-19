from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, index) for index, weight in enumerate(servers)]
        heapify(available)
        busy = []
        assignments = []
        current_time = 0

        for arrival, duration in enumerate(tasks):
            current_time = max(current_time, arrival)
            while busy and busy[0][0] <= current_time:
                _, weight, index = heappop(busy)
                heappush(available, (weight, index))

            if not available:
                current_time = busy[0][0]
                while busy and busy[0][0] <= current_time:
                    _, weight, index = heappop(busy)
                    heappush(available, (weight, index))

            weight, index = heappop(available)
            assignments.append(index)
            heappush(busy, (current_time + duration, weight, index))

        return assignments
