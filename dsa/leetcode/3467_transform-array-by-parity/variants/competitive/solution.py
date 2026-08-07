class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd_count = sum(value & 1 for value in nums)
        return [0] * (len(nums) - odd_count) + [1] * odd_count
