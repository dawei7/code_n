from math import isqrt


class Solution:
    def minOperations(self, k: int) -> int:
        value = isqrt(k)
        copies = (k + value - 1) // value
        return value + copies - 2
