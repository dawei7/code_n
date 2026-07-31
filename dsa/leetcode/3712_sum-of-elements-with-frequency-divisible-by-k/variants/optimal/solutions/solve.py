from collections import Counter


def solve(nums: list[int], k: int) -> int:
    frequencies = Counter(nums)
    return sum(value * frequency for value, frequency in frequencies.items() if frequency % k == 0)
