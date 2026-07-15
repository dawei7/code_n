from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        infinity = float("inf")
        distances = [[infinity] * n for _ in range(n)]

        for city in range(n):
            distances[city][city] = 0

        for first, second, weight in edges:
            distances[first][second] = weight
            distances[second][first] = weight

        for intermediate in range(n):
            through = distances[intermediate]
            for source in range(n):
                source_to_intermediate = distances[source][intermediate]
                if source_to_intermediate == infinity:
                    continue
                row = distances[source]
                for destination in range(n):
                    candidate = source_to_intermediate + through[destination]
                    if candidate < row[destination]:
                        row[destination] = candidate

        answer = -1
        fewest = n
        for city, row in enumerate(distances):
            reachable = sum(
                other != city and distance <= distanceThreshold
                for other, distance in enumerate(row)
            )
            if reachable <= fewest:
                fewest = reachable
                answer = city

        return answer
