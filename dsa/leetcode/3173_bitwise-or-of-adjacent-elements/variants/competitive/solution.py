class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [left | right for left, right in zip(nums, nums[1:])]
