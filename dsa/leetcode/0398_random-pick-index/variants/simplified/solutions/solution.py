import random
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.pos[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
