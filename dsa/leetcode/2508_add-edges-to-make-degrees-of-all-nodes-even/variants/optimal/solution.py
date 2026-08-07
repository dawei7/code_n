from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n + 1)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        odd = [node for node in range(1, n + 1) if len(graph[node]) % 2]
        if not odd:
            return True

        if len(odd) == 2:
            a, b = odd
            if b not in graph[a]:
                return True
            for middle in range(1, n + 1):
                if middle != a and middle != b and middle not in graph[a] and middle not in graph[b]:
                    return True
            return False

        if len(odd) == 4:
            a, b, c, d = odd
            return (
                (b not in graph[a] and d not in graph[c])
                or (c not in graph[a] and d not in graph[b])
                or (d not in graph[a] and c not in graph[b])
            )

        return False
