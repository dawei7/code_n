def solve(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    first = set(nums1)
    second = set(nums2)
    return [list(first - second), list(second - first)]
