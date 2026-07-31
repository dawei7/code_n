class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        modulo = 10**9 + 7
        n = len(nums)
        dp = [[0] * n for _ in range(1 << n)]
        for index in range(n):
            dp[1 << index][index] = 1

        for mask in range(1 << n):
            for last in range(n):
                ways = dp[mask][last]
                if ways == 0:
                    continue
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    if nums[last] % nums[nxt] == 0 or nums[nxt] % nums[last] == 0:
                        next_mask = mask | (1 << nxt)
                        dp[next_mask][nxt] = (dp[next_mask][nxt] + ways) % modulo

        return sum(dp[-1]) % modulo
