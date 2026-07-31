from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        values_above = set()

        for value in nums:
            if value < k:
                return -1
            if value > k:
                values_above.add(value)

        return len(values_above)
