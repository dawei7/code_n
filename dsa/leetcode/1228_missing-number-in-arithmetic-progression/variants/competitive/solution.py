from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        difference = (arr[-1] - arr[0]) // len(arr)
        if difference == 0:
            return arr[0]

        left, right = 0, len(arr) - 1
        while left < right:
            middle = (left + right) // 2
            expected = arr[0] + middle * difference
            if arr[middle] == expected:
                left = middle + 1
            else:
                right = middle
        return arr[0] + left * difference
