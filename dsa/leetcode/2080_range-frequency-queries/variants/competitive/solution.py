from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.positions = defaultdict(list)
        for index, value in enumerate(arr):
            self.positions[value].append(index)

    def query(self, left: int, right: int, value: int) -> int:
        positions = self.positions[value]
        return bisect_right(positions, right) - bisect_left(positions, left)
