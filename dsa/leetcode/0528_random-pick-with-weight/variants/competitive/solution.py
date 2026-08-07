from bisect import bisect_right
from itertools import accumulate
from random import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = list(accumulate(w))
        self.total = self.prefix_sums[-1]

    def pickIndex(self) -> int:
        return bisect_right(self.prefix_sums, random() * self.total)
