from collections import Counter


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        masks = [-1] * 31

        for value in range(2, 31):
            mask = 0
            for bit, prime in enumerate(primes):
                if value % (prime * prime) == 0:
                    break
                if value % prime == 0:
                    mask |= 1 << bit
            else:
                masks[value] = mask

        counts = Counter(nums)
        dp = [0] * (1 << len(primes))
        dp[0] = 1

        for value in range(2, 31):
            frequency = counts[value]
            value_mask = masks[value]
            if frequency == 0 or value_mask < 0:
                continue

            next_dp = dp[:]
            for used_mask, ways in enumerate(dp):
                if used_mask & value_mask == 0:
                    combined = used_mask | value_mask
                    next_dp[combined] = (next_dp[combined] + ways * frequency) % mod
            dp = next_dp

        return (sum(dp) * pow(2, counts[1], mod) - 1) % mod
