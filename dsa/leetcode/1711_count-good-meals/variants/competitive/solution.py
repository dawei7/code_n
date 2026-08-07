from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        modulo = 1_000_000_007
        seen = defaultdict(int)
        pairs = 0

        for value in deliciousness:
            power = 1
            while power <= 1 << 21:
                pairs += seen[power - value]
                power <<= 1
            seen[value] += 1

        return pairs % modulo
