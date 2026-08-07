class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        ways = 1
        previous_one = -1

        for index, value in enumerate(nums):
            if value == 0:
                continue
            if previous_one != -1:
                ways = ways * (index - previous_one) % modulus
            previous_one = index

        return ways if previous_one != -1 else 0
