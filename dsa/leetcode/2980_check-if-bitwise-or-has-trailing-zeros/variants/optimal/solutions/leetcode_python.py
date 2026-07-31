from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even_count = 0
        for value in nums:
            if value % 2 == 0:
                even_count += 1
                if even_count == 2:
                    return True
        return False
