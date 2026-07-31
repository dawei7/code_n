class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        best = 0

        for value in nums:
            remainder = value % k
            for previous in range(k):
                dp[previous][remainder] = dp[remainder][previous] + 1
                best = max(best, dp[previous][remainder])

        return best
