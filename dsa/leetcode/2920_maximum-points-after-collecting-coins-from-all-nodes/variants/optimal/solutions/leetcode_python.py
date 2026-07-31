from typing import List


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        parent = [-2] * n
        parent[0] = -1
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        maximum_shift = 14
        dp = [[0] * (maximum_shift + 1) for _ in range(n)]

        for node in reversed(order):
            for shift in range(maximum_shift - 1, -1, -1):
                keep_shift = (coins[node] >> shift) - k
                add_shift = coins[node] >> (shift + 1)

                for neighbor in graph[node]:
                    if parent[neighbor] == node:
                        keep_shift += dp[neighbor][shift]
                        add_shift += dp[neighbor][shift + 1]

                dp[node][shift] = max(keep_shift, add_shift)

        return dp[0][0]
