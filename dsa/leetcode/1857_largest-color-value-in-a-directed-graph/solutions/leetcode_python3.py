from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        node_count = len(colors)
        graph = [[] for _ in range(node_count)]
        indegree = [0] * node_count
        for source, target in edges:
            graph[source].append(target)
            indegree[target] += 1

        queue = deque(
            node for node, degree in enumerate(indegree) if degree == 0
        )
        counts = [[0] * 26 for _ in range(node_count)]
        processed = 0
        answer = 0

        while queue:
            node = queue.popleft()
            processed += 1
            color = ord(colors[node]) - ord("a")
            counts[node][color] += 1
            answer = max(answer, counts[node][color])

            for neighbor in graph[node]:
                for index in range(26):
                    counts[neighbor][index] = max(
                        counts[neighbor][index], counts[node][index]
                    )
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return answer if processed == node_count else -1
