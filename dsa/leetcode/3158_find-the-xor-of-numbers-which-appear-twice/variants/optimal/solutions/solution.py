from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = 0
        duplicates = 0

        for value in nums:
            bit = 1 << value
            if seen & bit:
                duplicates ^= value
            else:
                seen |= bit

        return duplicates
