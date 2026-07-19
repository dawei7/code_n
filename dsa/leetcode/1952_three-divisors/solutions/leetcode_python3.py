from math import isqrt


class Solution:
    def isThree(self, n: int) -> bool:
        root = isqrt(n)
        if root * root != n or root < 2:
            return False

        for divisor in range(2, isqrt(root) + 1):
            if root % divisor == 0:
                return False

        return True
