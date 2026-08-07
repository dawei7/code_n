from typing import List


class Solution:
    def maximumSubtreeSize(
        self,
        edges: List[List[int]],
        colors: List[int],
    ) -> int:
        node_count = len(colors)
        graph = [[] for _ in range(node_count)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        parent = [-1] * node_count
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                order.append(neighbor)

        sizes = [1] * node_count
        uniform = [True] * node_count
        answer = 1

        for node in reversed(order):
            for child in graph[node]:
                if parent[child] != node:
                    continue
                sizes[node] += sizes[child]
                if not uniform[child] or colors[child] != colors[node]:
                    uniform[node] = False

            if uniform[node]:
                answer = max(answer, sizes[node])

        return answer
