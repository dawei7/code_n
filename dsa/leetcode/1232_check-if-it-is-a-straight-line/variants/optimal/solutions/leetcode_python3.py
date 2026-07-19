from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0

        for x, y in coordinates[2:]:
            if (x - x0) * dy != (y - y0) * dx:
                return False
        return True
