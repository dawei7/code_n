from collections import Counter


def solve(nums: list[int], space: int) -> int:
    remainder_counts = Counter(value % space for value in nums)
    return min(nums, key=lambda value: (-remainder_counts[value % space], value))
