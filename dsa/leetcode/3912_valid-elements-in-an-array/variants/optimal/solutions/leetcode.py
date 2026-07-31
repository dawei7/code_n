class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        valid = [False] * n

        maximum = 0
        for index, value in enumerate(nums):
            if value > maximum:
                valid[index] = True
                maximum = value

        maximum = 0
        for index in range(n - 1, -1, -1):
            if nums[index] > maximum:
                valid[index] = True
                maximum = nums[index]

        return [value for index, value in enumerate(nums) if valid[index]]
