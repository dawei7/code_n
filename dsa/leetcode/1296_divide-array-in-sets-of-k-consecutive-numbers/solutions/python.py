from collections import Counter


def solve(nums, k):
    counts = Counter(nums)
    for start in sorted(counts):
        amount = counts[start]
        if amount == 0:
            continue
        for value in range(start, start + k):
            if counts[value] < amount:
                return False
            counts[value] -= amount
    return True
