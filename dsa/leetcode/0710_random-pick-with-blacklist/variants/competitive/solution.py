from random import randrange
from typing import List


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        blocked = set(blacklist)
        self.bound = n - len(blacklist)
        self.remap = {}
        replacement = self.bound

        for value in blacklist:
            if value >= self.bound:
                continue
            while replacement in blocked:
                replacement += 1
            self.remap[value] = replacement
            replacement += 1

    def pick(self) -> int:
        draw = randrange(self.bound)
        return self.remap.get(draw, draw)
