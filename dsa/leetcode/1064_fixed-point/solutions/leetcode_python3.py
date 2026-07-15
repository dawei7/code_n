from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)

        while left < right:
            middle = (left + right) // 2
            if arr[middle] < middle:
                left = middle + 1
            else:
                right = middle

        if left < len(arr) and arr[left] == left:
            return left
        return -1
