# Definition of commonBits API.
# def commonBits(num: int) -> int:
class Solution:
    def findNumber(self) -> int:
        zero_count = commonBits(0)
        answer = 0

        for bit in range(30):
            next_zero_count = commonBits(1 << bit)
            if next_zero_count > zero_count:
                answer |= 1 << bit
            zero_count = next_zero_count

        return answer
