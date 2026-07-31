def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    return sum(
        first % (second * k) == 0
        for first in nums1
        for second in nums2
    )
