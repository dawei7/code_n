from collections import defaultdict
from random import choice


class Solution:
    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for index, value in enumerate(nums):
            self.indices[value].append(index)

    def pick(self, target: int) -> int:
        return choice(self.indices[target])
