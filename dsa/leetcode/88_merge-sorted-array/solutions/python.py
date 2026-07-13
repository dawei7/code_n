def solve(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    first = m - 1
    second = n - 1
    destination = m + n - 1
    while second >= 0:
        if first >= 0 and nums1[first] > nums2[second]:
            nums1[destination] = nums1[first]
            first -= 1
        else:
            nums1[destination] = nums2[second]
            second -= 1
        destination -= 1
    return nums1
