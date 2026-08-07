from collections import deque
from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
            degree[first] += 1
            degree[second] += 1

        remaining_edges = n - 1
        leaves = deque(node for node in range(n) if degree[node] == 1 and coins[node] == 0)
        while leaves:
            leaf = leaves.popleft()
            degree[leaf] = 0
            for neighbor in graph[leaf]:
                if degree[neighbor] == 0:
                    continue
                degree[neighbor] -= 1
                remaining_edges -= 1
                if degree[neighbor] == 1 and coins[neighbor] == 0:
                    leaves.append(neighbor)

        leaves = deque(node for node in range(n) if degree[node] == 1)
        for _ in range(2):
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                degree[leaf] = 0
                for neighbor in graph[leaf]:
                    if degree[neighbor] == 0:
                        continue
                    degree[neighbor] -= 1
                    remaining_edges -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return max(0, 2 * remaining_edges)
