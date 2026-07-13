from collections import Counter


def solve(nums):
    counts = Counter(nums)
    return sum(counts[value] * (counts[value] - 1) // 2 for value in counts)
