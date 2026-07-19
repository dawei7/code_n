from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        frequencies = defaultdict(int)
        frequencies[0] = 1

        balance = 0
        smaller_prefixes = 0
        answer = 0

        for value in nums:
            if value == 1:
                smaller_prefixes += frequencies[balance]
                balance += 1
            else:
                balance -= 1
                smaller_prefixes -= frequencies[balance]

            answer = (answer + smaller_prefixes) % modulus
            frequencies[balance] += 1

        return answer
