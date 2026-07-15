import sys
from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        adjacency = [[] for _ in range(n)]
        for first, second in connections:
            adjacency[first].append(second)
            adjacency[second].append(first)

        discovery = [-1] * n
        low = [0] * n
        bridges = []
        timestamp = 0
        sys.setrecursionlimit(max(200_000, 2 * n + 10))

        def dfs(node: int, parent: int) -> None:
            nonlocal timestamp
            discovery[node] = timestamp
            low[node] = timestamp
            timestamp += 1

            for neighbor in adjacency[node]:
                if neighbor == parent:
                    continue
                if discovery[neighbor] == -1:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > discovery[node]:
                        bridges.append([node, neighbor])
                else:
                    low[node] = min(low[node], discovery[neighbor])

        dfs(0, -1)
        return bridges
