from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        best = -1
        for index in range(len(arr) - 1, -1, -1):
            original = arr[index]
            arr[index] = best
            best = max(best, original)
        return arr
