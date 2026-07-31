from collections import deque
from typing import List


class Solution:
    def minimumThreshold(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        target: int,
        k: int,
    ) -> int:
        if source == target:
            return 0

        graph = [[] for _ in range(n)]
        thresholds = {0}
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
            thresholds.add(weight)

        candidates = sorted(thresholds)

        def is_possible(threshold: int) -> bool:
            heavy_edges = [k + 1] * n
            heavy_edges[source] = 0
            queue = deque([source])

            while queue:
                node = queue.popleft()
                for neighbor, weight in graph[node]:
                    cost = int(weight > threshold)
                    next_count = heavy_edges[node] + cost
                    if next_count >= heavy_edges[neighbor] or next_count > k:
                        continue

                    heavy_edges[neighbor] = next_count
                    if cost == 0:
                        queue.appendleft(neighbor)
                    else:
                        queue.append(neighbor)

            return heavy_edges[target] <= k

        if not is_possible(candidates[-1]):
            return -1

        left, right = 0, len(candidates) - 1
        while left < right:
            middle = (left + right) // 2
            if is_possible(candidates[middle]):
                right = middle
            else:
                left = middle + 1

        return candidates[left]
