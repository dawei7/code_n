from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
        if graph[destination]:
            return False
        state = [0] * n

        def dfs(node: int) -> bool:
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            if not graph[node]:
                return node == destination
            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            return True

        return dfs(source)
