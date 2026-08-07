class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minimum_index = 0
        maximum_index = 0
        for index in range(1, len(nums)):
            if nums[index] < nums[minimum_index]:
                minimum_index = index
            if nums[index] >= nums[maximum_index]:
                maximum_index = index
        return minimum_index + len(nums) - 1 - maximum_index - (minimum_index > maximum_index)
