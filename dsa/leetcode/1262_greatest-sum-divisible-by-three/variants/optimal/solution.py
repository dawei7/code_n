from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float("-inf"), float("-inf")]
        for value in nums:
            current = dp[:]
            for residue in range(3):
                destination = (residue + value) % 3
                current[destination] = max(current[destination], dp[residue] + value)
            dp = current
        return dp[0]
