from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        closest = [float("inf")] * 26
        conflict_radius = float("inf")

        for (x, y), tag in zip(points, s):
            radius = max(abs(x), abs(y))
            tag_index = ord(tag) - ord("a")

            if radius < closest[tag_index]:
                conflict_radius = min(conflict_radius, closest[tag_index])
                closest[tag_index] = radius
            else:
                conflict_radius = min(conflict_radius, radius)

        return sum(radius < conflict_radius for radius in closest)
