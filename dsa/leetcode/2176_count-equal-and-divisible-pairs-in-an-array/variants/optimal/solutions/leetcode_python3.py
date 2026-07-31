from collections import Counter, defaultdict
from math import gcd
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_counts = defaultdict(Counter)
        answer = 0

        for index, value in enumerate(nums):
            current_gcd = gcd(index, k)
            answer += sum(
                count
                for previous_gcd, count in gcd_counts[value].items()
                if (current_gcd * previous_gcd) % k == 0
            )
            gcd_counts[value][current_gcd] += 1

        return answer
