from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        latest_by_reversed_value = {}
        minimum = len(nums)

        for index, value in enumerate(nums):
            previous = latest_by_reversed_value.get(value)
            if previous is not None:
                minimum = min(minimum, index - previous)
                if minimum == 1:
                    return 1

            reversed_value = 0
            remaining = value
            while remaining:
                reversed_value = reversed_value * 10 + remaining % 10
                remaining //= 10
            latest_by_reversed_value[reversed_value] = index

        return -1 if minimum == len(nums) else minimum
