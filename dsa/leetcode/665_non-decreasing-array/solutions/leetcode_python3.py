class Solution:
    def checkPossibility(self, nums):
        changes = 0
        for index in range(1, len(nums)):
            if nums[index - 1] <= nums[index]:
                continue
            changes += 1
            if changes > 1:
                return False
            if index == 1 or nums[index - 2] <= nums[index]:
                nums[index - 1] = nums[index]
            else:
                nums[index] = nums[index - 1]
        return True
