class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 1_000_000_007

        if sum(nums) < 2 * k:
            return 0

        ways_by_sum = [0] * k
        ways_by_sum[0] = 1

        for value in nums:
            for subtotal in range(k - 1, value - 1, -1):
                ways_by_sum[subtotal] = (
                    ways_by_sum[subtotal] + ways_by_sum[subtotal - value]
                ) % mod

        bad_groups = sum(ways_by_sum) % mod
        return (pow(2, len(nums), mod) - 2 * bad_groups) % mod
