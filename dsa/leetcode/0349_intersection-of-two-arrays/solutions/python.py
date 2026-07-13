def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    candidates = set(nums1)
    return list({value for value in nums2 if value in candidates})
