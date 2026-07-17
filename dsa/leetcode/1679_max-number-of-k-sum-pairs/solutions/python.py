from collections import Counter


def solve(nums: list[int], k: int) -> int:
    unmatched: Counter[int] = Counter()
    operations = 0

    for value in nums:
        complement = k - value
        if unmatched[complement] > 0:
            unmatched[complement] -= 1
            operations += 1
        else:
            unmatched[value] += 1

    return operations
