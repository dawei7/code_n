from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        ordered = sorted(nums)
        left = 0
        longest = 1

        for right, maximum in enumerate(ordered):
            while maximum > k * ordered[left]:
                left += 1
            longest = max(longest, right - left + 1)

        return len(nums) - longest
