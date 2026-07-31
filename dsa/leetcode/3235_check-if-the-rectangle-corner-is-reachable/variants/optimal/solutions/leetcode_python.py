from typing import List


class Solution:
    def canReachCorner(
        self,
        xCorner: int,
        yCorner: int,
        circles: List[List[int]],
    ) -> bool:
        count = len(circles)
        top_or_left = count
        bottom_or_right = count + 1
        parent = list(range(count + 2))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first: int, second: int) -> None:
            first_root = find(first)
            second_root = find(second)
            if first_root != second_root:
                parent[first_root] = second_root

        for index, (x, y, radius) in enumerate(circles):
            radius_squared = radius * radius
            above = max(0, y - yCorner)
            right = max(0, x - xCorner)

            touches_left = x * x + above * above <= radius_squared
            touches_top = right * right + (y - yCorner) ** 2 <= radius_squared
            touches_right = (x - xCorner) ** 2 + above * above <= radius_squared
            touches_bottom = right * right + y * y <= radius_squared

            if touches_left or touches_top:
                union(index, top_or_left)
            if touches_bottom or touches_right:
                union(index, bottom_or_right)

            for other in range(index):
                other_x, other_y, other_radius = circles[other]
                radius_sum = radius + other_radius
                if (
                    (x - other_x) ** 2 + (y - other_y) ** 2
                    <= radius_sum * radius_sum
                    and x * other_radius + other_x * radius
                    < xCorner * radius_sum
                    and y * other_radius + other_y * radius
                    < yCorner * radius_sum
                ):
                    union(index, other)

            if find(top_or_left) == find(bottom_or_right):
                return False

        return True
