class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        limit = max(nums)
        present = bytearray(limit + 1)
        for value in nums:
            present[value] = 1

        smallest_divisor = [0] * (limit + 1)
        for divisor in range(1, limit + 1):
            if not present[divisor]:
                continue
            for multiple in range(divisor, limit + 1, divisor):
                if present[multiple] and smallest_divisor[multiple] == 0:
                    smallest_divisor[multiple] = divisor

        return sum(smallest_divisor[value] for value in nums)
