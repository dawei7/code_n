from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        greater = []

        for value in nums:
            if value < pivot:
                smaller.append(value)
            elif value == pivot:
                equal.append(value)
            else:
                greater.append(value)

        return smaller + equal + greater
