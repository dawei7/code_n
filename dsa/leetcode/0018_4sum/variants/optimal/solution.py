from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for first in range(len(nums) - 3):
            if first and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums) - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                left, right = second + 1, len(nums) - 1
                while left < right:
                    total = nums[first] + nums[second] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[first], nums[second], nums[left], nums[right]])
                        left_value, right_value = nums[left], nums[right]
                        while left < right and nums[left] == left_value:
                            left += 1
                        while left < right and nums[right] == right_value:
                            right -= 1
        return result
