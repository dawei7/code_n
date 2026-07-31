from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for city_a, city_b, travel_cost in roads:
            city_a -= 1
            city_b -= 1
            graph[city_a].append((city_b, travel_cost))
            graph[city_b].append((city_a, travel_cost))

        answer = appleCost[:]
        heap = [(cost, city) for city, cost in enumerate(answer)]
        heapify(heap)
        round_trip_factor = k + 1

        while heap:
            cost, city = heappop(heap)
            if cost != answer[city]:
                continue

            for neighbor, travel_cost in graph[city]:
                candidate = cost + round_trip_factor * travel_cost
                if candidate < answer[neighbor]:
                    answer[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))

        return answer
