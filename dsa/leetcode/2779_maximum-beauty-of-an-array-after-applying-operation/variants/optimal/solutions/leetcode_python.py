class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        best = 0

        for right, value in enumerate(nums):
            while value - nums[left] > 2 * k:
                left += 1
            best = max(best, right - left + 1)

        return best
