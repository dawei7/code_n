from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []

        remaining = Counter(changed)
        original = []

        for value in sorted(changed):
            if remaining[value] == 0:
                continue
            if remaining[2 * value] == 0:
                return []

            original.append(value)
            remaining[value] -= 1
            remaining[2 * value] -= 1

        return original
