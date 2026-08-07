from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [(index ^ (index >> 1)) ^ start for index in range(1 << n)]
