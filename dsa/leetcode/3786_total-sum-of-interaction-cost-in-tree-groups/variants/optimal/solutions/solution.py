from collections import Counter
from typing import List


class Solution:
    def interactionCosts(
        self,
        n: int,
        edges: List[List[int]],
        group: List[int],
    ) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                order.append(neighbor)

        totals = Counter(group)
        subtree = [[0] * 21 for _ in range(n)]
        answer = 0

        for node in reversed(order):
            subtree[node][group[node]] += 1
            if parent[node] == -1:
                continue

            parent_counts = subtree[parent[node]]
            for label in range(1, 21):
                count = subtree[node][label]
                answer += count * (totals[label] - count)
                parent_counts[label] += count

        return answer
