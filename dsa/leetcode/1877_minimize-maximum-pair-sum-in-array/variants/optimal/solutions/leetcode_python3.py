from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[index] + nums[-index - 1]
            for index in range(len(nums) // 2)
        )
