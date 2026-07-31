from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        left_sum = nums[left]
        right_sum = nums[right]
        operations = 0

        while left < right:
            if left_sum == right_sum:
                left += 1
                right -= 1
                if left < right:
                    left_sum = nums[left]
                    right_sum = nums[right]
            elif left_sum < right_sum:
                left += 1
                left_sum += nums[left]
                operations += 1
            else:
                right -= 1
                right_sum += nums[right]
                operations += 1

        return operations
