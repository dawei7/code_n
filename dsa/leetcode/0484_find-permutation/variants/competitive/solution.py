from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        permutation = list(range(1, len(s) + 2))
        run_start = 0

        for boundary in range(len(s) + 1):
            if boundary < len(s) and s[boundary] == "D":
                continue
            left = run_start
            right = boundary
            while left < right:
                permutation[left], permutation[right] = permutation[right], permutation[left]
                left += 1
                right -= 1
            run_start = boundary + 1

        return permutation
