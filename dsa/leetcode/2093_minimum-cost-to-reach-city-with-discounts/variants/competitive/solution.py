import heapq
from typing import List


class Solution:
    def minimumCost(
        self,
        n: int,
        highways: List[List[int]],
        discounts: int,
    ) -> int:
        graph = [[] for _ in range(n)]
        for city1, city2, toll in highways:
            graph[city1].append((city2, toll))
            graph[city2].append((city1, toll))

        infinity = float("inf")
        distances = [[infinity] * (discounts + 1) for _ in range(n)]
        distances[0][0] = 0
        queue = [(0, 0, 0)]

        while queue:
            cost, city, used = heapq.heappop(queue)
            if cost != distances[city][used]:
                continue
            if city == n - 1:
                return cost

            for neighbor, toll in graph[city]:
                full_cost = cost + toll
                if full_cost < distances[neighbor][used]:
                    distances[neighbor][used] = full_cost
                    heapq.heappush(queue, (full_cost, neighbor, used))

                if used < discounts:
                    discounted_cost = cost + toll // 2
                    if discounted_cost < distances[neighbor][used + 1]:
                        distances[neighbor][used + 1] = discounted_cost
                        heapq.heappush(
                            queue,
                            (discounted_cost, neighbor, used + 1),
                        )

        return -1
