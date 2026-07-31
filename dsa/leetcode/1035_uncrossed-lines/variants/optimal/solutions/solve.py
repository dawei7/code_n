"""Optimal app-local solution for LeetCode 1035."""


def solve(nums1, nums2):
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1

    previous = [0] * (len(nums2) + 1)
    for value1 in nums1:
        current = [0] * (len(nums2) + 1)
        for index, value2 in enumerate(nums2, start=1):
            if value1 == value2:
                current[index] = previous[index - 1] + 1
            else:
                current[index] = max(previous[index], current[index - 1])
        previous = current
    return previous[-1]
