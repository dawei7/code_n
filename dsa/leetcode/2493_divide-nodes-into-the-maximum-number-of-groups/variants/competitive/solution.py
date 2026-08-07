from collections import deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for node_a, node_b in edges:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        color = [0] * (n + 1)
        components = []

        for start in range(1, n + 1):
            if color[start] != 0:
                continue

            color[start] = 1
            component = []
            queue = deque([start])

            while queue:
                node = queue.popleft()
                component.append(node)

                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return -1

            components.append(component)

        answer = 0
        for component in components:
            maximum_groups = 0

            for start in component:
                distance = [-1] * (n + 1)
                distance[start] = 0
                queue = deque([start])
                farthest = 0

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if distance[neighbor] == -1:
                            distance[neighbor] = distance[node] + 1
                            farthest = max(farthest, distance[neighbor])
                            queue.append(neighbor)

                maximum_groups = max(maximum_groups, farthest + 1)

            answer += maximum_groups

        return answer
