class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        present = set(nums)
        return [
            value
            for value in range(min(nums), max(nums) + 1)
            if value not in present
        ]
