from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = 1
        down = 1
        best = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
                up = 1
            else:
                up = 1
                down = 1
            best = max(best, up, down)

        return best
