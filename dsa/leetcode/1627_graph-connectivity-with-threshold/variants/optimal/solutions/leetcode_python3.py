from typing import List


class Solution:
    def areConnected(
        self, n: int, threshold: int, queries: List[List[int]]
    ) -> List[bool]:
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(left: int, right: int) -> None:
            left_root = find(left)
            right_root = find(right)
            if left_root == right_root:
                return
            if size[left_root] < size[right_root]:
                left_root, right_root = right_root, left_root
            parent[right_root] = left_root
            size[left_root] += size[right_root]

        for divisor in range(threshold + 1, n + 1):
            for multiple in range(divisor * 2, n + 1, divisor):
                union(divisor, multiple)

        return [find(left) == find(right) for left, right in queries]
