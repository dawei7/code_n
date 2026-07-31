from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        frequency = [0] * (len(A) + 1)
        common = 0
        prefix_common = []

        for value_a, value_b in zip(A, B):
            for value in (value_a, value_b):
                frequency[value] += 1
                if frequency[value] == 2:
                    common += 1
            prefix_common.append(common)

        return prefix_common
