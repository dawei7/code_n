"""Optimal solution for LeetCode 373: Find K Pairs with Smallest Sums."""

from heapq import heapify, heappop, heappush


def solve(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    if not nums1 or not nums2 or k <= 0:
        return []

    heap = [
        (nums1[index] + nums2[0], index, 0)
        for index in range(min(k, len(nums1)))
    ]
    heapify(heap)
    pairs: list[list[int]] = []

    while heap and len(pairs) < k:
        _, left_index, right_index = heappop(heap)
        pairs.append([nums1[left_index], nums2[right_index]])
        if right_index + 1 < len(nums2):
            next_right = right_index + 1
            heappush(
                heap,
                (nums1[left_index] + nums2[next_right], left_index, next_right),
            )

    return pairs

