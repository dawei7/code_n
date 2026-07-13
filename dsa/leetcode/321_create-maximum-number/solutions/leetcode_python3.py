from typing import List


def _maximum_subsequence(nums: List[int], length: int) -> List[int]:
    drops = len(nums) - length
    stack = []
    for digit in nums:
        while drops and stack and stack[-1] < digit:
            stack.pop()
            drops -= 1
        stack.append(digit)
    return stack[:length]


def _suffix_is_greater(
    left: List[int], left_index: int, right: List[int], right_index: int
) -> bool:
    while (
        left_index < len(left)
        and right_index < len(right)
        and left[left_index] == right[right_index]
    ):
        left_index += 1
        right_index += 1
    return right_index == len(right) or (
        left_index < len(left) and left[left_index] > right[right_index]
    )


def _merge_maximum(left: List[int], right: List[int]) -> List[int]:
    merged = []
    left_index = right_index = 0
    while left_index < len(left) or right_index < len(right):
        if _suffix_is_greater(left, left_index, right, right_index):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    return merged


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        best = []
        first_minimum = max(0, k - len(nums2))
        first_maximum = min(k, len(nums1))
        for take_from_first in range(first_minimum, first_maximum + 1):
            left = _maximum_subsequence(nums1, take_from_first)
            right = _maximum_subsequence(nums2, k - take_from_first)
            candidate = _merge_maximum(left, right)
            if candidate > best:
                best = candidate
        return best
