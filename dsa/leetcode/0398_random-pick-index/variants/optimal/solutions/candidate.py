"""Proposed app-local solution for LeetCode 398: Random Pick Index."""

from collections import defaultdict
from random import choice


class Solution:
    def __init__(self, nums: list[int]):
        self.indices = defaultdict(list)
        for i, x in enumerate(nums):
            self.indices[x].append(i)

    def pick(self, target: int) -> int:
        return choice(self.indices[target])


def solve(nums: list[int], targets: list[int]) -> list[int]:
    solution = Solution(nums)
    return [solution.pick(target) for target in targets]
