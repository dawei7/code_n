"""Optimal app-local solution for LeetCode 398: Random Pick Index."""

from collections import defaultdict
from random import choice


def solve(nums: list[int], targets: list[int]) -> list[int]:
    indices: dict[int, list[int]] = defaultdict(list)
    for index, value in enumerate(nums):
        indices[value].append(index)

    return [choice(indices[target]) for target in targets]
