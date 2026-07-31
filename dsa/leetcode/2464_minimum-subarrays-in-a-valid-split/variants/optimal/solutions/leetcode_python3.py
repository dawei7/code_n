from math import isqrt
from typing import List


class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        maximum = max(nums)
        smallest_factor = list(range(maximum + 1))

        for factor in range(2, isqrt(maximum) + 1):
            if smallest_factor[factor] != factor:
                continue
            for multiple in range(factor * factor, maximum + 1, factor):
                if smallest_factor[multiple] == multiple:
                    smallest_factor[multiple] = factor

        n = len(nums)
        infinity = n + 1
        splits = [0] + [infinity] * n
        best_start = {}

        for index, value in enumerate(nums):
            factors = []
            remaining = value
            while remaining > 1:
                prime = smallest_factor[remaining]
                factors.append(prime)
                while remaining % prime == 0:
                    remaining //= prime

            for prime in factors:
                best_start[prime] = min(
                    best_start.get(prime, infinity), splits[index]
                )

            if factors:
                splits[index + 1] = 1 + min(
                    best_start[prime] for prime in factors
                )

        return -1 if splits[n] > n else splits[n]
