from math import floor, sqrt
from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        maximum_x = max(tower[0] for tower in towers)
        maximum_y = max(tower[1] for tower in towers)
        radius_squared = radius * radius
        best = [0, 0]
        best_quality = -1

        for x in range(maximum_x + 1):
            for y in range(maximum_y + 1):
                quality = 0
                for tower_x, tower_y, tower_quality in towers:
                    distance_squared = (x - tower_x) ** 2 + (y - tower_y) ** 2
                    if distance_squared <= radius_squared:
                        quality += floor(tower_quality / (1 + sqrt(distance_squared)))
                if quality > best_quality:
                    best_quality = quality
                    best = [x, y]

        return best
