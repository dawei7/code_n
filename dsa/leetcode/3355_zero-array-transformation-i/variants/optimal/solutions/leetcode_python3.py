class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        difference = [0] * (len(nums) + 1)
        for left, right in queries:
            difference[left] += 1
            difference[right + 1] -= 1

        coverage = 0
        for value, change in zip(nums, difference):
            coverage += change
            if coverage < value:
                return False

        return True
