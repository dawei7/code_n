from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        parent = list(range(n))
        rank = [0] * n

        def find(i: int) -> int:
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def union(i: int, j: int) -> None:
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                if rank[root_i] == rank[root_j]:
                    rank[root_i] += 1

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
