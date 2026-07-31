from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for frequency in Counter(nums).values():
            if frequency == 1:
                return -1
            operations += (frequency + 2) // 3
        return operations
