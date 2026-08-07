import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = [[] for _ in range(n)]
        for (first, second), probability in zip(edges, succProb):
            graph[first].append((second, probability))
            graph[second].append((first, probability))

        best = [0.0] * n
        best[start_node] = 1.0
        heap = [(-1.0, start_node)]

        while heap:
            negative_probability, node = heapq.heappop(heap)
            probability = -negative_probability
            if node == end_node:
                return probability
            if probability < best[node]:
                continue

            for neighbor, edge_probability in graph[node]:
                candidate = probability * edge_probability
                if candidate > best[neighbor]:
                    best[neighbor] = candidate
                    heapq.heappush(heap, (-candidate, neighbor))

        return 0.0
