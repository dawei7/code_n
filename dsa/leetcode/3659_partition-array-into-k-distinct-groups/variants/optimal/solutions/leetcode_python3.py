from collections import Counter
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False

        group_count = len(nums) // k
        return max(Counter(nums).values()) <= group_count
