class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] + [float('inf')] * n

        for right in range(n):
            frequency = [0] * n
            trimmed_length = 0

            for left in range(right, -1, -1):
                value = nums[left]
                frequency[value] += 1

                if frequency[value] == 2:
                    trimmed_length += 2
                elif frequency[value] > 2:
                    trimmed_length += 1

                dp[right + 1] = min(
                    dp[right + 1],
                    dp[left] + k + trimmed_length,
                )

        return dp[n]
