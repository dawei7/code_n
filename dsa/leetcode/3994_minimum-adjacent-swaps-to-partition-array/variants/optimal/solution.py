class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 1_000_000_007
        middle = 0
        high = 0
        swaps = 0

        for value in nums:
            if value < a:
                swaps += middle + high
            elif value <= b:
                swaps += high
                middle += 1
            else:
                high += 1

        return swaps % MOD
