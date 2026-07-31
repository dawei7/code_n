class Solution:
    def isReachableAtTime(
        self, sx: int, sy: int, fx: int, fy: int, t: int
    ) -> bool:
        horizontal = abs(sx - fx)
        vertical = abs(sy - fy)
        if horizontal == 0 and vertical == 0 and t == 1:
            return False
        return max(horizontal, vertical) <= t
