class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return sum(nums[i] != nums[i + 1] for i in range(len(nums) - 1))


def solve(nums: list[int]) -> int:
    return Solution().minOperations(nums)
