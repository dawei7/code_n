from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjacency = defaultdict(list)
        balance = defaultdict(int)

        for start, end in pairs:
            adjacency[start].append(end)
            balance[start] += 1
            balance[end] -= 1

        trail_start = pairs[0][0]
        for vertex, difference in balance.items():
            if difference == 1:
                trail_start = vertex
                break

        stack = [trail_start]
        reversed_vertices = []
        while stack:
            vertex = stack[-1]
            if adjacency[vertex]:
                stack.append(adjacency[vertex].pop())
            else:
                reversed_vertices.append(stack.pop())

        vertices = reversed_vertices[::-1]
        return [[vertices[index], vertices[index + 1]] for index in range(len(pairs))]
