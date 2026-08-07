from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ordered = sorted(nums, key=lambda value: (len(value), value))
        return ordered[-k]
