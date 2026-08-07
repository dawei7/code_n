class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        index = 0
        while index < len(nums):
            start = index
            while index + 1 < len(nums) and nums[index + 1] == nums[index] + 1:
                index += 1
            if start == index:
                ranges.append(str(nums[start]))
            else:
                ranges.append(f"{nums[start]}->{nums[index]}")
            index += 1
        return ranges
