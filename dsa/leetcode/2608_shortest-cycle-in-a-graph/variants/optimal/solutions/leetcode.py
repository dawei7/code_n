from collections import deque
from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        shortest = n + 1
        for start in range(n):
            distance = [-1] * n
            parent = [-1] * n
            distance[start] = 0
            queue = deque([start])

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distance[neighbor] == -1:
                        distance[neighbor] = distance[node] + 1
                        parent[neighbor] = node
                        queue.append(neighbor)
                    elif parent[node] != neighbor:
                        shortest = min(
                            shortest,
                            distance[node] + distance[neighbor] + 1,
                        )

        return -1 if shortest == n + 1 else shortest
