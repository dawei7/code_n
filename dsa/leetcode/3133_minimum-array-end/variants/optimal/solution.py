class Solution:
    def minEnd(self, n: int, x: int) -> int:
        remaining = n - 1
        answer = x
        bit = 1

        while remaining:
            if answer & bit == 0:
                if remaining & 1:
                    answer |= bit
                remaining >>= 1
            bit <<= 1

        return answer
