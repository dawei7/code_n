from collections import Counter


def solve(nums: list[int]) -> list[int]:
    frequency = Counter(nums)
    return sorted(nums, key=lambda value: (frequency[value], -value))
