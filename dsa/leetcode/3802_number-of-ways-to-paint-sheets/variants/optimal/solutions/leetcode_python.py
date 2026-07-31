from bisect import bisect_right
from typing import List


class Solution:
    def numberOfWays(self, n: int, limit: List[int]) -> int:
        modulo = 1_000_000_007
        threshold = n - 1
        capacities = sorted(min(value, threshold) for value in limit)
        color_count = len(capacities)

        prefix = [0]
        for value in capacities:
            prefix.append(prefix[-1] + value)

        ways = 0
        for value in capacities:
            first = bisect_right(capacities, threshold - value)
            partner_count = color_count - first
            ways += (
                partner_count * (value - threshold)
                + prefix[color_count]
                - prefix[first]
            )
            ways -= max(0, 2 * value - threshold)

        return ways % modulo
