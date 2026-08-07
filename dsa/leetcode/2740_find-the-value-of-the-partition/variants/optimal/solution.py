class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(right - left for left, right in zip(nums, nums[1:]))
