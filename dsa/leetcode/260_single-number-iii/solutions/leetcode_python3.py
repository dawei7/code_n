from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        combined = 0
        for value in nums:
            combined ^= value
        distinguishing_bit = combined & -combined
        first = 0
        second = 0
        for value in nums:
            if value & distinguishing_bit:
                first ^= value
            else:
                second ^= value
        return [first, second]
