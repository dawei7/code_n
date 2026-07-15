from typing import List


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = [(cost, 0, house) for house, cost in enumerate(wells, start=1)]
        edges.extend((cost, first, second) for first, second, cost in pipes)
        edges.sort()
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        total = 0
        accepted = 0
        for cost, first, second in edges:
            first_root = find(first)
            second_root = find(second)
            if first_root == second_root:
                continue
            if size[first_root] < size[second_root]:
                first_root, second_root = second_root, first_root
            parent[second_root] = first_root
            size[first_root] += size[second_root]
            total += cost
            accepted += 1
            if accepted == n:
                break
        return total
