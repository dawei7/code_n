class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        answer = len(nums) + 1

        for left in range(len(nums)):
            value = 0
            for right in range(left, len(nums)):
                value |= nums[right]
                if value >= k:
                    answer = min(answer, right - left + 1)
                    break

        return -1 if answer > len(nums) else answer
