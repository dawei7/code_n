class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        current = 1
        longest = 1
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return longest

