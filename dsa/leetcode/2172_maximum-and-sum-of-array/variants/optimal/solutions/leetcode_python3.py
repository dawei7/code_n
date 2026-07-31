from functools import lru_cache
from typing import List


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        powers = [3**slot for slot in range(numSlots)]

        @lru_cache(None)
        def best(index: int, mask: int) -> int:
            if index == len(nums):
                return 0

            answer = 0
            for slot, power in enumerate(powers, start=1):
                if (mask // power) % 3 < 2:
                    answer = max(
                        answer,
                        (nums[index] & slot)
                        + best(index + 1, mask + power),
                    )
            return answer

        return best(0, 0)
