class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 10**9 + 7
        required = [-1] * n
        for end, count in requirements:
            required[end] = count

        max_inversions = max(count for _, count in requirements)
        dp = [0] * (max_inversions + 1)
        dp[0] = 1

        for length in range(1, n + 1):
            next_dp = [0] * (max_inversions + 1)
            window = 0

            for inversions in range(max_inversions + 1):
                window += dp[inversions]
                if inversions >= length:
                    window -= dp[inversions - length]
                next_dp[inversions] = window % mod

            target = required[length - 1]
            if target != -1:
                ways = next_dp[target]
                next_dp = [0] * (max_inversions + 1)
                next_dp[target] = ways

            dp = next_dp

        return dp[required[n - 1]]
