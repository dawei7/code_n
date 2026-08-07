from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [value ^ (value >> 1) for value in range(1 << n)]
