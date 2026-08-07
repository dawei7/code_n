from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        first = len(arr1) - 1
        second = len(arr2) - 1
        carry = 0
        result = []

        while first >= 0 or second >= 0 or carry:
            carry += arr1[first] if first >= 0 else 0
            carry += arr2[second] if second >= 0 else 0
            result.append(carry & 1)
            carry = -(carry >> 1)
            first -= 1
            second -= 1

        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]
