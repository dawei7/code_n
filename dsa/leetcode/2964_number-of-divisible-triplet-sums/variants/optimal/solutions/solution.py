from collections import defaultdict
from typing import List


class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        singles = defaultdict(int)
        pairs = defaultdict(int)
        answer = 0

        for value in nums:
            remainder = value % d
            answer += pairs[(-remainder) % d]
            for previous, count in singles.items():
                pairs[(previous + remainder) % d] += count
            singles[remainder] += 1

        return answer
