from math import gcd


class Solution:
    def numGoodSubarrays(self, nums: list[int], k: int) -> int:
        remainder_frequency = {0: 1}
        remainder = 0
        occurrence_count = 0
        for value in nums:
            remainder = (remainder + value) % k
            occurrence_count += remainder_frequency.get(remainder, 0)
            remainder_frequency[remainder] = remainder_frequency.get(remainder, 0) + 1

        duplicate_count = 0
        run_start = 0
        while run_start < len(nums):
            run_end = run_start + 1
            while run_end < len(nums) and nums[run_end] == nums[run_start]:
                run_end += 1

            run_length = run_end - run_start
            divisible_length_step = k // gcd(nums[run_start], k)
            divisible_length_count = run_length // divisible_length_step
            duplicate_count += (
                divisible_length_count * run_length
                - divisible_length_step * divisible_length_count * (divisible_length_count + 1) // 2
            )
            run_start = run_end

        return occurrence_count - duplicate_count
