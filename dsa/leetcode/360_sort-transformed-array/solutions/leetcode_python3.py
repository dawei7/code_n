from typing import List


class Solution:
    def sortTransformedArray(
        self, nums: List[int], a: int, b: int, c: int
    ) -> List[int]:
        def transform(value: int) -> int:
            return a * value * value + b * value + c

        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        if a >= 0:
            write = len(nums) - 1
            while left <= right:
                left_value = transform(nums[left])
                right_value = transform(nums[right])
                if left_value > right_value:
                    result[write] = left_value
                    left += 1
                else:
                    result[write] = right_value
                    right -= 1
                write -= 1
        else:
            write = 0
            while left <= right:
                left_value = transform(nums[left])
                right_value = transform(nums[right])
                if left_value < right_value:
                    result[write] = left_value
                    left += 1
                else:
                    result[write] = right_value
                    right -= 1
                write += 1

        return result

