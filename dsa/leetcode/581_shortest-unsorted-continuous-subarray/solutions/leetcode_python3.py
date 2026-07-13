class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        left = 0
        right = -1
        prefix_max = float("-inf")
        suffix_min = float("inf")

        for index in range(len(nums)):
            if nums[index] < prefix_max:
                right = index
            else:
                prefix_max = nums[index]

            reverse_index = len(nums) - 1 - index
            if nums[reverse_index] > suffix_min:
                left = reverse_index
            else:
                suffix_min = nums[reverse_index]

        return 0 if right == -1 else right - left + 1

