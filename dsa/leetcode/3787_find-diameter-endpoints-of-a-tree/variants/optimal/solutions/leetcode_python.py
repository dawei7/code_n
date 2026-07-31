from collections import deque
from typing import List


class Solution:
    def findSpecialNodes(self, n: int, edges: List[List[int]]) -> str:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def distances(start: int) -> List[int]:
            distance = [-1] * n
            distance[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distance[neighbor] == -1:
                        distance[neighbor] = distance[node] + 1
                        queue.append(neighbor)
            return distance

        from_zero = distances(0)
        endpoint_a = max(range(n), key=from_zero.__getitem__)
        from_a = distances(endpoint_a)
        endpoint_b = max(range(n), key=from_a.__getitem__)
        from_b = distances(endpoint_b)
        diameter = from_a[endpoint_b]

        return "".join(
            "1" if max(from_a[node], from_b[node]) == diameter else "0"
            for node in range(n)
        )
