from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        starts = sorted(start for start, _ in flowers)
        ends = sorted(end for _, end in flowers)
        return [
            bisect_right(starts, time) - bisect_left(ends, time)
            for time in people
        ]
