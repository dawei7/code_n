from random import randrange
from typing import List


class Solution:
    def __init__(self, m: int, n: int):
        self.rows = m
        self.cols = n
        self.total = m * n
        self.remaining = self.total
        self.remap = {}

    def flip(self) -> List[int]:
        ticket = randrange(self.remaining)
        selected = self.remap.get(ticket, ticket)
        self.remaining -= 1
        self.remap[ticket] = self.remap.get(self.remaining, self.remaining)
        self.remap.pop(self.remaining, None)
        return [selected // self.cols, selected % self.cols]

    def reset(self) -> None:
        self.remaining = self.total
        self.remap.clear()
