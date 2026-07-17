from typing import List


class Solution:
    def countSubgraphsForEachDiameter(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            first -= 1
            second -= 1
            graph[first].append(second)
            graph[second].append(first)

        def farthest(start: int, mask: int) -> tuple[int, int, int]:
            stack = [(start, -1, 0)]
            farthest_city = start
            farthest_distance = 0
            visited = 0
            while stack:
                city, parent, distance = stack.pop()
                visited += 1
                if distance > farthest_distance:
                    farthest_city = city
                    farthest_distance = distance
                for neighbor in graph[city]:
                    if neighbor != parent and mask & (1 << neighbor):
                        stack.append((neighbor, city, distance + 1))
            return farthest_city, farthest_distance, visited

        answer = [0] * (n - 1)
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            start = (mask & -mask).bit_length() - 1
            endpoint, _, visited = farthest(start, mask)
            if visited != mask.bit_count():
                continue
            _, diameter, _ = farthest(endpoint, mask)
            answer[diameter - 1] += 1

        return answer
