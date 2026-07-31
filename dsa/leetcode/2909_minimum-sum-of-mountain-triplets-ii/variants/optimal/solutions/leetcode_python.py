from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        suffix_minimum = nums[:]
        for index in range(len(nums) - 2, -1, -1):
            suffix_minimum[index] = min(nums[index], suffix_minimum[index + 1])

        answer = float("inf")
        prefix_minimum = nums[0]
        for middle in range(1, len(nums) - 1):
            right_minimum = suffix_minimum[middle + 1]
            if prefix_minimum < nums[middle] and right_minimum < nums[middle]:
                answer = min(answer, prefix_minimum + nums[middle] + right_minimum)
            prefix_minimum = min(prefix_minimum, nums[middle])

        return -1 if answer == float("inf") else int(answer)
