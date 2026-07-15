from collections import deque
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        vertex_count = len(edges) + 1
        adjacency = [[] for _ in range(vertex_count)]
        for left, right in edges:
            adjacency[left].append(right)
            adjacency[right].append(left)

        def farthest(start: int):
            distances = [-1] * vertex_count
            distances[start] = 0
            queue = deque([start])
            endpoint = start
            while queue:
                vertex = queue.popleft()
                endpoint = vertex
                for neighbor in adjacency[vertex]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = distances[vertex] + 1
                        queue.append(neighbor)
            return endpoint, distances[endpoint]

        endpoint, _ = farthest(0)
        _, diameter = farthest(endpoint)
        return diameter
