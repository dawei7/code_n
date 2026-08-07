from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for value in nums:
            if value % 2 == 0:
                result |= value
        return result
