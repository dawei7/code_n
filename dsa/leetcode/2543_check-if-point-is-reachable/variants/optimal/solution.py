from math import gcd


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        common_divisor = gcd(targetX, targetY)
        return (common_divisor & (common_divisor - 1)) == 0
