class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        return len({current for current, desired in zip(nums, target) if current != desired})
