class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                operations += 1
        return operations if nums[-2] == nums[-1] == 1 else -1
