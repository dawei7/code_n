from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for first, second in dislikes:
            graph[first].append(second)
            graph[second].append(first)

        colors = [0] * (n + 1)
        for person in range(1, n + 1):
            if colors[person] != 0:
                continue
            colors[person] = 1
            stack = [person]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[current]
                        stack.append(neighbor)
                    elif colors[neighbor] == colors[current]:
                        return False
        return True
