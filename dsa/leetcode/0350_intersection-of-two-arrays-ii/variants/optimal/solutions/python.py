from collections import Counter


def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    remaining = Counter(nums1)
    result: list[int] = []
    for value in nums2:
        if remaining[value] > 0:
            result.append(value)
            remaining[value] -= 1
    return result
