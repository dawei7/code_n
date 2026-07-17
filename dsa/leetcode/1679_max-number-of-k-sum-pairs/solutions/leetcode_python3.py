from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        unmatched = Counter()
        operations = 0

        for value in nums:
            complement = k - value
            if unmatched[complement] > 0:
                unmatched[complement] -= 1
                operations += 1
            else:
                unmatched[value] += 1

        return operations
