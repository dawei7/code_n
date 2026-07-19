from bisect import bisect_right
from random import randrange
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0
        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)
        self.total = total

    def pick(self) -> List[int]:
        ticket = randrange(self.total)
        rectangle_index = bisect_right(self.prefix, ticket)
        previous_total = self.prefix[rectangle_index - 1] if rectangle_index else 0
        offset = ticket - previous_total
        x1, y1, x2, _ = self.rects[rectangle_index]
        width = x2 - x1 + 1
        return [x1 + offset % width, y1 + offset // width]
