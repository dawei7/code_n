from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for city_a, city_b, distance in roads:
            graph[city_a].append((city_b, distance))
            graph[city_b].append((city_a, distance))

        answer = float("inf")
        seen = {1}
        stack = [1]
        while stack:
            city = stack.pop()
            for neighbor, distance in graph[city]:
                answer = min(answer, distance)
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return answer
