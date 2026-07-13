from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        heap = [
            (nums1[index] + nums2[0], index, 0)
            for index in range(min(k, len(nums1)))
        ]
        heapify(heap)
        pairs = []

        while heap and len(pairs) < k:
            _, left_index, right_index = heappop(heap)
            pairs.append([nums1[left_index], nums2[right_index]])
            if right_index + 1 < len(nums2):
                next_right = right_index + 1
                heappush(
                    heap,
                    (
                        nums1[left_index] + nums2[next_right],
                        left_index,
                        next_right,
                    ),
                )

        return pairs

