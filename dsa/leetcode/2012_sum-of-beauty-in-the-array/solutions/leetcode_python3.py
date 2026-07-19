from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        length = len(nums)
        suffix_minimum = [float("inf")] * (length + 1)

        for index in range(length - 1, -1, -1):
            suffix_minimum[index] = min(
                nums[index], suffix_minimum[index + 1]
            )

        beauty = 0
        prefix_maximum = nums[0]
        for index in range(1, length - 1):
            if prefix_maximum < nums[index] < suffix_minimum[index + 1]:
                beauty += 2
            elif nums[index - 1] < nums[index] < nums[index + 1]:
                beauty += 1
            prefix_maximum = max(prefix_maximum, nums[index])

        return beauty
