def solve(nums1, nums2):
    keep = len(nums1) // 2
    values1 = set(nums1)
    values2 = set(nums2)
    return min(
        len(values1 | values2),
        min(len(values1), keep) + min(len(values2), keep),
    )
