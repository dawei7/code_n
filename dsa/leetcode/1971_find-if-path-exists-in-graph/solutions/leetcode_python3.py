from collections import deque
from typing import List


class Solution:
    def validPath(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
    ) -> bool:
        adjacency = [[] for _ in range(n)]
        for left, right in edges:
            adjacency[left].append(right)
            adjacency[right].append(left)

        queue = deque([source])
        seen = [False] * n
        seen[source] = True

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in adjacency[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    queue.append(neighbor)

        return False
