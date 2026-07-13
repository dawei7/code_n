from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        dp = [0.0] * (n + 1)
        for end in range(1, n + 1):
            dp[end] = prefix[end] / end

        for groups in range(2, k + 1):
            next_dp = [0.0] * (n + 1)
            for end in range(groups, n + 1):
                next_dp[end] = max(
                    dp[split] + (prefix[end] - prefix[split]) / (end - split)
                    for split in range(groups - 1, end)
                )
            dp = next_dp
        return dp[n]
