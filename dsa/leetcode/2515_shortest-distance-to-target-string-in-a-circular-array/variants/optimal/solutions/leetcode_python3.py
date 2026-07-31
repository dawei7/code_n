from typing import List


class Solution:
    def closestTarget(
        self, words: List[str], target: str, startIndex: int
    ) -> int:
        length = len(words)
        best = length + 1

        for index, word in enumerate(words):
            if word != target:
                continue
            direct_distance = abs(index - startIndex)
            best = min(best, direct_distance, length - direct_distance)

        return -1 if best == length + 1 else best
