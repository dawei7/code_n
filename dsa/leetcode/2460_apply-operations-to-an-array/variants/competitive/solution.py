from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for index in range(n - 1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0

        write = 0
        for value in nums:
            if value != 0:
                nums[write] = value
                write += 1

        while write < n:
            nums[write] = 0
            write += 1

        return nums
