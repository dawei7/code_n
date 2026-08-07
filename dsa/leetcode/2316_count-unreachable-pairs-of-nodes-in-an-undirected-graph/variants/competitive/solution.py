from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        seen = [False] * n
        remaining = n
        answer = 0

        for start in range(n):
            if seen[start]:
                continue
            seen[start] = True
            stack = [start]
            size = 0
            while stack:
                node = stack.pop()
                size += 1
                for neighbor in graph[node]:
                    if not seen[neighbor]:
                        seen[neighbor] = True
                        stack.append(neighbor)
            remaining -= size
            answer += size * remaining

        return answer
