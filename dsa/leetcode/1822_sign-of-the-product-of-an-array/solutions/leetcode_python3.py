from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for value in nums:
            if value == 0:
                return 0
            if value < 0:
                sign = -sign
        return sign
