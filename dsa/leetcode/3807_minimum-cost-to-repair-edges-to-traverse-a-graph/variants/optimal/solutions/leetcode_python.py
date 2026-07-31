from collections import deque
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        graph = [[] for _ in range(n)]
        for first, second, cost in edges:
            graph[first].append((second, cost))
            graph[second].append((first, cost))

        costs = sorted({cost for _, _, cost in edges})

        def can_reach(limit: int) -> bool:
            distance = [-1] * n
            distance[0] = 0
            queue = deque([0])

            while queue:
                node = queue.popleft()
                if distance[node] == k:
                    continue

                for neighbor, cost in graph[node]:
                    if cost <= limit and distance[neighbor] == -1:
                        distance[neighbor] = distance[node] + 1
                        if neighbor == n - 1:
                            return True
                        queue.append(neighbor)

            return False

        if not can_reach(costs[-1]):
            return -1

        left = 0
        right = len(costs) - 1

        while left < right:
            middle = (left + right) // 2
            if can_reach(costs[middle]):
                right = middle
            else:
                left = middle + 1

        return costs[left]
