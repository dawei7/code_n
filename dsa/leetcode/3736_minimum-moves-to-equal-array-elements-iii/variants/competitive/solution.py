class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        return maximum * len(nums) - sum(nums)
