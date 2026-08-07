from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for source, destination in edges:
            graph[source].append(destination)

        ancestors = [[] for _ in range(n)]
        for ancestor in range(n):
            seen = [False] * n
            stack = [ancestor]

            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if not seen[neighbor]:
                        seen[neighbor] = True
                        ancestors[neighbor].append(ancestor)
                        stack.append(neighbor)

        return ancestors
