from bisect import bisect_left
from typing import List


class Solution:
    def findTheDistanceValue(
        self,
        arr1: List[int],
        arr2: List[int],
        d: int,
    ) -> int:
        sorted_arr2 = sorted(arr2)
        qualifying = 0

        for value in arr1:
            position = bisect_left(sorted_arr2, value)
            right_is_far = (
                position == len(sorted_arr2)
                or sorted_arr2[position] - value > d
            )
            left_is_far = (
                position == 0
                or value - sorted_arr2[position - 1] > d
            )
            if left_is_far and right_is_far:
                qualifying += 1

        return qualifying
