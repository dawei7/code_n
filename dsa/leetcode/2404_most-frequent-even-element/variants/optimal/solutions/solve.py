from collections import Counter


def solve(nums: list[int]) -> int:
    counts = Counter(value for value in nums if value % 2 == 0)
    if not counts:
        return -1
    return min(counts, key=lambda value: (-counts[value], value))
