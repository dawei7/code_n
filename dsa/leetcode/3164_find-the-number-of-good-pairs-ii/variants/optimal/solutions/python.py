from collections import Counter


def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    limit = max(nums1) // k
    frequency = [0] * (limit + 1)

    for value in nums1:
        if value % k == 0:
            frequency[value // k] += 1

    total = 0
    for divisor, copies in Counter(nums2).items():
        for multiple in range(divisor, limit + 1, divisor):
            total += frequency[multiple] * copies

    return total
