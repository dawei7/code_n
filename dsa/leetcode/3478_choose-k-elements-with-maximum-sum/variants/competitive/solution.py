from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        indices = sorted(range(len(nums1)), key=nums1.__getitem__)
        answer = [0] * len(nums1)
        largest_values = []
        largest_sum = 0

        group_start = 0
        while group_start < len(indices):
            group_end = group_start + 1
            group_value = nums1[indices[group_start]]
            while group_end < len(indices) and nums1[indices[group_end]] == group_value:
                group_end += 1

            for position in range(group_start, group_end):
                answer[indices[position]] = largest_sum

            for position in range(group_start, group_end):
                value = nums2[indices[position]]
                heappush(largest_values, value)
                largest_sum += value
                if len(largest_values) > k:
                    largest_sum -= heappop(largest_values)

            group_start = group_end

        return answer
