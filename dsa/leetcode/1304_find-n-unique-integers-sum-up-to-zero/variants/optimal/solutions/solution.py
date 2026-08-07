from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] * n
        idx = 0
        for i in range(1, n // 2 + 1):
            res[idx] = i
            res[idx + 1] = -i
            idx += 2
        return res
