from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapify(blocks)
        while len(blocks) > 1:
            heappop(blocks)
            larger = heappop(blocks)
            heappush(blocks, larger + split)
        return blocks[0]
