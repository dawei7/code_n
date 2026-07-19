from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        ordered = sorted(arr)
        difference = ordered[1] - ordered[0]
        return all(
            ordered[index] - ordered[index - 1] == difference
            for index in range(2, len(ordered))
        )
