def solve(nums1: list[int], nums2: list[int]) -> int:
    first = 0
    second = 0

    while first < len(nums1) and second < len(nums2):
        if nums1[first] == nums2[second]:
            return nums1[first]
        if nums1[first] < nums2[second]:
            first += 1
        else:
            second += 1

    return -1
