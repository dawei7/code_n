from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first: int, second: int) -> bool:
            first_root = find(first)
            second_root = find(second)
            if first_root == second_root:
                return False
            if size[first_root] < size[second_root]:
                first_root, second_root = second_root, first_root
            parent[second_root] = first_root
            size[first_root] += size[second_root]
            return True

        ordered_edges = sorted(edges, key=lambda edge: edge[2], reverse=True)
        index = 0

        while index < len(ordered_edges):
            time = ordered_edges[index][2]

            while index < len(ordered_edges) and ordered_edges[index][2] == time:
                first, second, _ = ordered_edges[index]
                if union(first, second):
                    components -= 1
                index += 1

            if components < k:
                return time

        return 0
