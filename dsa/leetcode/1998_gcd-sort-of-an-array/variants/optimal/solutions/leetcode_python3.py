from math import isqrt
from typing import List


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        maximum = max(nums)
        parent = list(range(maximum + 1))

        def find(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        def union(first: int, second: int) -> None:
            first_root = find(first)
            second_root = find(second)
            if first_root != second_root:
                parent[first_root] = second_root

        smallest_factor = list(range(maximum + 1))
        for factor in range(2, isqrt(maximum) + 1):
            if smallest_factor[factor] != factor:
                continue
            for multiple in range(factor * factor, maximum + 1, factor):
                if smallest_factor[multiple] == multiple:
                    smallest_factor[multiple] = factor

        for value in nums:
            remaining = value
            while remaining > 1:
                prime = smallest_factor[remaining]
                union(value, prime)
                while remaining % prime == 0:
                    remaining //= prime

        return all(
            find(value) == find(target)
            for value, target in zip(nums, sorted(nums))
        )
