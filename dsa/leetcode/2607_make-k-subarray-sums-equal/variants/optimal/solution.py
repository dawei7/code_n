from math import gcd
from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        group_count = gcd(len(arr), k)
        operations = 0

        for start in range(group_count):
            group = sorted(arr[start::group_count])
            median = group[len(group) // 2]
            operations += sum(abs(value - median) for value in group)

        return operations
