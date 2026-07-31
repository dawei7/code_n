from collections import Counter


def solve(nums: list[int]) -> list[int]:
    frequencies = Counter(nums)
    return [
        value
        for value, count in frequencies.items()
        if count == 1 and value - 1 not in frequencies and value + 1 not in frequencies
    ]
