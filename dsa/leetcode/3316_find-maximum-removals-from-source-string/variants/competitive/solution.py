from typing import List


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        removable = [False] * len(source)
        for index in targetIndices:
            removable[index] = True

        infinity = len(targetIndices) + 1
        minimum_kept = [infinity] * (len(pattern) + 1)
        minimum_kept[0] = 0

        for index, character in enumerate(source):
            for matched in range(len(pattern) - 1, -1, -1):
                if character == pattern[matched]:
                    minimum_kept[matched + 1] = min(
                        minimum_kept[matched + 1],
                        minimum_kept[matched] + removable[index],
                    )

        return len(targetIndices) - minimum_kept[-1]
