from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        size = [1] * n

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for left, right in edges:
            left_root = find(left)
            right_root = find(right)
            if left_root == right_root:
                return False
            if size[left_root] < size[right_root]:
                left_root, right_root = right_root, left_root
            parent[right_root] = left_root
            size[left_root] += size[right_root]
        return True
