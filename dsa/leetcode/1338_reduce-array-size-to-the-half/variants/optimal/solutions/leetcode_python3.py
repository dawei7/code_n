from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        target = len(arr) // 2
        removed = 0

        for selected, frequency in enumerate(
            sorted(Counter(arr).values(), reverse=True), start=1
        ):
            removed += frequency
            if removed >= target:
                return selected

        raise AssertionError("A legal input must reach its removal target")
