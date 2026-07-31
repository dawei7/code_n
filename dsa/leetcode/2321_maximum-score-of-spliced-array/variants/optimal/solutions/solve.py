from typing import List


def solve(nums1: List[int], nums2: List[int]) -> int:
    def greatest_gain(target: List[int], source: List[int]) -> int:
        ending_here = 0
        best = 0
        for target_value, source_value in zip(target, source):
            ending_here = max(0, ending_here + source_value - target_value)
            best = max(best, ending_here)
        return best

    return max(
        sum(nums1) + greatest_gain(nums1, nums2),
        sum(nums2) + greatest_gain(nums2, nums1),
    )
