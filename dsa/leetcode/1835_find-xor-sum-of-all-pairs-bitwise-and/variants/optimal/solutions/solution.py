from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        first_xor = 0
        for value in arr1:
            first_xor ^= value

        second_xor = 0
        for value in arr2:
            second_xor ^= value

        return first_xor & second_xor
