from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            middle = (left + right) // 2
            if arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle

        return left
