from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        first = 0
        answer = 0

        for second, value in enumerate(nums2):
            while first < len(nums1) and nums1[first] > value:
                first += 1

            if first == len(nums1):
                break
            if first <= second:
                answer = max(answer, second - first)

        return answer
