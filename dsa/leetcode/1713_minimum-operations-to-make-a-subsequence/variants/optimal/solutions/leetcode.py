from bisect import bisect_left
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        target_index = {value: index for index, value in enumerate(target)}
        tails = []

        for value in arr:
            if value not in target_index:
                continue
            index = target_index[value]
            position = bisect_left(tails, index)
            if position == len(tails):
                tails.append(index)
            else:
                tails[position] = index

        return len(target) - len(tails)
