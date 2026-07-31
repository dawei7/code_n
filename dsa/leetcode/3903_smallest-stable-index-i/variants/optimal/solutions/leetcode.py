class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_minimum = [0] * n
        suffix_minimum[-1] = nums[-1]

        for index in range(n - 2, -1, -1):
            suffix_minimum[index] = min(nums[index], suffix_minimum[index + 1])

        prefix_maximum = nums[0]
        for index, value in enumerate(nums):
            prefix_maximum = max(prefix_maximum, value)
            if prefix_maximum - suffix_minimum[index] <= k:
                return index

        return -1
