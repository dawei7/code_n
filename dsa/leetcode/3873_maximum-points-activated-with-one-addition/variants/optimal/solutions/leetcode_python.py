class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        size = [1] * n

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a: int, b: int) -> None:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        x_owner = {}
        y_owner = {}

        for i, (x, y) in enumerate(points):
            if x in x_owner:
                union(i, x_owner[x])
            else:
                x_owner[x] = i

            if y in y_owner:
                union(i, y_owner[y])
            else:
                y_owner[y] = i

        largest = 0
        second_largest = 0

        for i in range(n):
            if find(i) != i:
                continue
            component_size = size[i]
            if component_size > largest:
                second_largest = largest
                largest = component_size
            elif component_size > second_largest:
                second_largest = component_size

        return largest + second_largest + 1
