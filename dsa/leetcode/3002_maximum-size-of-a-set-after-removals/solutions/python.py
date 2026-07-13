def solve(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    set1 = set(nums1)
    set2 = set(nums2)

    cap = n // 2
    common = len(set1 & set2)
    only1 = len(set1) - common
    only2 = len(set2) - common

    keep1 = min(only1, cap)
    keep2 = min(only2, cap)
    shared_capacity = (cap - keep1) + (cap - keep2)
    return keep1 + keep2 + min(common, shared_capacity)
