from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        city_count = len(roads) + 1
        graph = [[] for _ in range(city_count)]
        for city_a, city_b in roads:
            graph[city_a].append(city_b)
            graph[city_b].append(city_a)

        parent = [-1] * city_count
        order = [0]
        for city in order:
            for neighbor in graph[city]:
                if neighbor == parent[city]:
                    continue
                parent[neighbor] = city
                order.append(neighbor)

        representatives = [1] * city_count
        fuel = 0
        for city in reversed(order[1:]):
            fuel += (representatives[city] + seats - 1) // seats
            representatives[parent[city]] += representatives[city]

        return fuel
