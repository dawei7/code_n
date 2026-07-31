from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for value in range(1, n // 2 + 1):
            result.extend((value, -value))
        if n % 2:
            result.append(0)
        return result
