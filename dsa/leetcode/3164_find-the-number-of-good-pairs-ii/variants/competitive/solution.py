from collections import Counter


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        limit = max(nums1) // k
        frequency = [0] * (limit + 1)

        for value in nums1:
            if value % k == 0:
                frequency[value // k] += 1

        total = 0
        for divisor, copies in Counter(nums2).items():
            for multiple in range(divisor, limit + 1, divisor):
                total += frequency[multiple] * copies

        return total
