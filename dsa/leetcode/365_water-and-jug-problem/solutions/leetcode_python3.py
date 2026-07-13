class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target == 0:
            return True
        if target > x + y:
            return False

        left = x
        right = y
        while right:
            left, right = right, left % right
        return target % left == 0

