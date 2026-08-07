from collections import defaultdict
from typing import List


class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        modulo = 1_000_000_007
        ending = {}
        answer = 0

        for first, second in zip(nums1, nums2):
            current = defaultdict(int)
            current[first] += 1
            current[-second] += 1

            for difference, count in ending.items():
                current[difference + first] = (current[difference + first] + count) % modulo
                current[difference - second] = (current[difference - second] + count) % modulo

            ending = current
            answer = (answer + ending[0]) % modulo

        return answer
