def solve(nums1: list[int], nums2: list[int]) -> int:
    def required_swaps(maximum1: int, maximum2: int) -> int:
        swaps = 0
        for value1, value2 in zip(nums1[:-1], nums2[:-1]):
            if value1 <= maximum1 and value2 <= maximum2:
                continue
            if value2 <= maximum1 and value1 <= maximum2:
                swaps += 1
            else:
                return len(nums1) + 1
        return swaps

    keep_last = required_swaps(nums1[-1], nums2[-1])
    swap_last = 1 + required_swaps(nums2[-1], nums1[-1])
    answer = min(keep_last, swap_last)
    return -1 if answer > len(nums1) else answer
