from typing import List


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(city: int) -> int:
            while city != parent[city]:
                parent[city] = parent[parent[city]]
                city = parent[city]
            return city

        total = 0
        used = 0
        for city_a, city_b, cost in sorted(connections, key=lambda edge: edge[2]):
            root_a = find(city_a)
            root_b = find(city_b)
            if root_a == root_b:
                continue
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
            total += cost
            used += 1
            if used == n - 1:
                return total
        return total if used == n - 1 else -1
