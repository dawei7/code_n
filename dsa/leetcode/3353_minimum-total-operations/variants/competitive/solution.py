class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum(nums[i] != nums[i + 1] for i in range(len(nums) - 1))
