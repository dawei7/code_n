from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[city + 1] for city in range(n - 1)] + [[]]
        answer = []

        for source, destination in queries:
            graph[source].append(destination)
            distance = [-1] * n
            distance[0] = 0
            queue = deque([0])

            while queue:
                city = queue.popleft()
                for neighbor in graph[city]:
                    if distance[neighbor] == -1:
                        distance[neighbor] = distance[city] + 1
                        queue.append(neighbor)

            answer.append(distance[n - 1])

        return answer
