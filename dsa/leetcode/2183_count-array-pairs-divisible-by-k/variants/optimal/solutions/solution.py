from collections import Counter
from math import gcd
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_counts = Counter()
        answer = 0

        for value in nums:
            current_gcd = gcd(value, k)
            answer += sum(count for previous_gcd, count in gcd_counts.items() if (current_gcd * previous_gcd) % k == 0)
            gcd_counts[current_gcd] += 1

        return answer
