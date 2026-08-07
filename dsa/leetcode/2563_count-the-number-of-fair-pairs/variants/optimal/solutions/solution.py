class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count_at_most(limit: int) -> int:
            left = 0
            right = len(nums) - 1
            pairs = 0

            while left < right:
                if nums[left] + nums[right] <= limit:
                    pairs += right - left
                    left += 1
                else:
                    right -= 1

            return pairs

        return count_at_most(upper) - count_at_most(lower - 1)
