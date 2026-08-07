from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        prefix_maximum = 0
        for index, value in enumerate(arr):
            prefix_maximum = max(prefix_maximum, value)
            if prefix_maximum == index:
                chunks += 1
        return chunks
