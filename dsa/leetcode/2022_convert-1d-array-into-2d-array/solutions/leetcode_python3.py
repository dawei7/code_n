from typing import List


class Solution:
    def construct2DArray(
        self, original: List[int], m: int, n: int
    ) -> List[List[int]]:
        if len(original) != m * n:
            return []
        return [original[start : start + n] for start in range(0, len(original), n)]
