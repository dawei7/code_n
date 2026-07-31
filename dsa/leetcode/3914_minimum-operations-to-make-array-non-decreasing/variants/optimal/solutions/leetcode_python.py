class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return sum(
            max(0, left - right)
            for left, right in zip(nums, nums[1:])
        )
