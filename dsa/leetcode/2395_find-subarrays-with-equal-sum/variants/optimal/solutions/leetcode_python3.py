from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen_sums = set()

        for index in range(len(nums) - 1):
            pair_sum = nums[index] + nums[index + 1]
            if pair_sum in seen_sums:
                return True
            seen_sums.add(pair_sum)

        return False
