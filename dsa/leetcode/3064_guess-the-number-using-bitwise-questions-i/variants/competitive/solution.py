# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:
class Solution:
    def findNumber(self) -> int:
        answer = 0

        for bit in range(30):
            mask = 1 << bit
            if commonSetBits(mask) > 0:
                answer |= mask

        return answer
