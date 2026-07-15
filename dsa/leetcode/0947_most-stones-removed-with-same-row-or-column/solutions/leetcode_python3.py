from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))
        size = [1] * n

        def find(index):
            while parent[index] != index:
                parent[index] = parent[parent[index]]
                index = parent[index]
            return index

        def union(left, right):
            left_root = find(left)
            right_root = find(right)
            if left_root == right_root:
                return
            if size[left_root] < size[right_root]:
                left_root, right_root = right_root, left_root
            parent[right_root] = left_root
            size[left_root] += size[right_root]

        row_owner = {}
        column_owner = {}
        for index, (row, column) in enumerate(stones):
            if row in row_owner:
                union(index, row_owner[row])
            else:
                row_owner[row] = index
            if column in column_owner:
                union(index, column_owner[column])
            else:
                column_owner[column] = index

        components = len({find(index) for index in range(n)})
        return n - components
