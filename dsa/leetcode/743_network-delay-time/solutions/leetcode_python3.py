import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for source, destination, travel_time in times:
            graph[source].append((destination, travel_time))

        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        queue = [(0, k)]

        while queue:
            distance, node = heapq.heappop(queue)
            if distance != distances[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heapq.heappush(queue, (candidate, neighbor))

        delay = max(distances[1:])
        return -1 if delay == float("inf") else delay
