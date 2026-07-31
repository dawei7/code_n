from typing import List


class Solution:
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        blocked = set(restricted)
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        seen = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in blocked and neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return len(seen)
