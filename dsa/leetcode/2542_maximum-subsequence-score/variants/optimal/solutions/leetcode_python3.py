import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        selected = []
        selected_sum = 0
        answer = 0

        for second, first in sorted(zip(nums2, nums1), reverse=True):
            heapq.heappush(selected, first)
            selected_sum += first

            if len(selected) > k:
                selected_sum -= heapq.heappop(selected)

            if len(selected) == k:
                answer = max(answer, selected_sum * second)

        return answer
