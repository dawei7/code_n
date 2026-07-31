from collections import Counter, defaultdict
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        size = len(vals)
        adjacency = [[] for _ in range(size)]
        for first, second in edges:
            adjacency[first].append(second)
            adjacency[second].append(first)

        nodes_by_value = defaultdict(list)
        for node, value in enumerate(vals):
            nodes_by_value[value].append(node)

        parent = list(range(size))
        component_size = [1] * size

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first: int, second: int) -> None:
            first_root = find(first)
            second_root = find(second)
            if first_root == second_root:
                return
            if component_size[first_root] < component_size[second_root]:
                first_root, second_root = second_root, first_root
            parent[second_root] = first_root
            component_size[first_root] += component_size[second_root]

        answer = 0
        for value in sorted(nodes_by_value):
            for node in nodes_by_value[value]:
                for neighbor in adjacency[node]:
                    if vals[neighbor] <= value:
                        union(node, neighbor)

            counts = Counter(find(node) for node in nodes_by_value[value])
            answer += sum(count * (count + 1) // 2 for count in counts.values())

        return answer
