"""Optimal solution for LeetCode 1035: Uncrossed Lines."""


def solve(nums1: list[int], nums2: list[int]) -> int:
    previous = [0] * (len(nums2) + 1)
    for value1 in nums1:
        current = [0] * (len(nums2) + 1)
        for j, value2 in enumerate(nums2, start=1):
            if value1 == value2:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(previous[j], current[j - 1])
        previous = current
    return previous[-1]
