class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        candidates = []

        for index, value in enumerate(nums):
            if not candidates or value > nums[candidates[-1]]:
                candidates.append(index)

        answer = 0

        for right in range(len(nums) - 1, -1, -1):
            while candidates and candidates[-1] >= right:
                candidates.pop()

            while candidates and nums[candidates[-1]] > nums[right]:
                left = candidates.pop()
                answer = max(answer, right - left + 1)

        return answer
