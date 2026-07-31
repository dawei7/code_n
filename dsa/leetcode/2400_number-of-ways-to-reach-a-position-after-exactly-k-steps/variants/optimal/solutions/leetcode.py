from math import comb


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        displacement = endPos - startPos
        if abs(displacement) > k or (k + displacement) % 2:
            return 0

        right_steps = (k + displacement) // 2
        return comb(k, right_steps) % 1_000_000_007
