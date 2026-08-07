from heapq import heappop, heappush
from typing import List


class Solution:
    def countRestrictedPaths(
        self,
        n: int,
        edges: List[List[int]],
    ) -> int:
        graph = [[] for _ in range(n)]
        for first, second, weight in edges:
            first -= 1
            second -= 1
            graph[first].append((second, weight))
            graph[second].append((first, weight))

        distances = [float("inf")] * n
        distances[n - 1] = 0
        heap = [(0, n - 1)]

        while heap:
            distance, node = heappop(heap)
            if distance != distances[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))

        modulo = 1_000_000_007
        ways = [0] * n
        ways[n - 1] = 1

        for node in sorted(range(n), key=distances.__getitem__):
            for neighbor, _ in graph[node]:
                if distances[neighbor] > distances[node]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % modulo

        return ways[0]
