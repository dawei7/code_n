class Solution:
    def numberOfComponents(self, properties: list[list[int]], k: int) -> int:
        masks = []
        for row in properties:
            mask = 0
            for value in row:
                mask |= 1 << value
            masks.append(mask)

        n = len(properties)
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for left in range(n):
            for right in range(left + 1, n):
                if (masks[left] & masks[right]).bit_count() < k:
                    continue

                root_left = find(left)
                root_right = find(right)
                if root_left == root_right:
                    continue

                if size[root_left] < size[root_right]:
                    root_left, root_right = root_right, root_left
                parent[root_right] = root_left
                size[root_left] += size[root_right]
                components -= 1

        return components


def solve(properties: list[list[int]], k: int) -> int:
    return Solution().numberOfComponents(properties, k)
