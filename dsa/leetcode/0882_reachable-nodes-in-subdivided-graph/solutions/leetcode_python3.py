import heapq
from typing import List


class Solution:
    def reachableNodes(
        self, edges: List[List[int]], maxMoves: int, n: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for first, second, subdivisions in edges:
            weight = subdivisions + 1
            graph[first].append((second, weight))
            graph[second].append((first, weight))

        distances = [float("inf")] * n
        distances[0] = 0
        queue = [(0, 0)]
        while queue:
            distance, node = heapq.heappop(queue)
            if distance != distances[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heapq.heappush(queue, (candidate, neighbor))

        reachable = sum(distance <= maxMoves for distance in distances)
        for first, second, subdivisions in edges:
            from_first = max(0, maxMoves - distances[first])
            from_second = max(0, maxMoves - distances[second])
            reachable += min(subdivisions, from_first + from_second)
        return reachable
