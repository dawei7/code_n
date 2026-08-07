from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [
            index
            for index in range(1, len(mountain) - 1)
            if mountain[index - 1] < mountain[index] > mountain[index + 1]
        ]
