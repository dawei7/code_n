from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [{} for _ in nums]
        best = 2

        for i, value in enumerate(nums):
            for j in range(i):
                difference = value - nums[j]
                candidate = dp[j].get(difference, 1) + 1
                dp[i][difference] = max(dp[i].get(difference, 0), candidate)
                best = max(best, dp[i][difference])

        return best

