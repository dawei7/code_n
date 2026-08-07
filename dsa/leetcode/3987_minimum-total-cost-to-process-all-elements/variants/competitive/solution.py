class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        operations = (sum(nums) - 1) // k
        return operations * (operations + 1) // 2 % 1_000_000_007
