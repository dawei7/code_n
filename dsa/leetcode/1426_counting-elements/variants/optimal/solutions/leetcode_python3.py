from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        values = set(arr)
        return sum(value + 1 in values for value in arr)
