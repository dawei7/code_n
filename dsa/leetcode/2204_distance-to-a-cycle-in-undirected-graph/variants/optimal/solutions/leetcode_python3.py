from collections import deque
from typing import List


class Solution:
    def distanceToCycle(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
            degree[first] += 1
            degree[second] += 1

        leaves = deque(node for node in range(n) if degree[node] == 1)
        while leaves:
            node = leaves.popleft()
            degree[node] = 0
            for neighbor in graph[node]:
                if degree[neighbor] == 0:
                    continue
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    leaves.append(neighbor)

        distance = [-1] * n
        queue = deque()
        for node in range(n):
            if degree[node] > 0:
                distance[node] = 0
                queue.append(node)

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distance[neighbor] != -1:
                    continue
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

        return distance
