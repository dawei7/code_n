class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        closest_x = min(max(xCenter, x1), x2)
        closest_y = min(max(yCenter, y1), y2)
        delta_x = xCenter - closest_x
        delta_y = yCenter - closest_y
        return delta_x * delta_x + delta_y * delta_y <= radius * radius
