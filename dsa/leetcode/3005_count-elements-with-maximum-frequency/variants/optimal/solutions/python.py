from collections import Counter


def solve(nums):
    frequencies = Counter(nums)
    maximum = max(frequencies.values())
    return sum(count for count in frequencies.values() if count == maximum)
