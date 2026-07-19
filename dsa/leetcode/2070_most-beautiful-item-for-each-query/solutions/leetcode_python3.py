from bisect import bisect_right
from typing import List


class Solution:
    def maximumBeauty(
        self, items: List[List[int]], queries: List[int]
    ) -> List[int]:
        items.sort()
        prices = []
        prefix_beauty = []
        best = 0

        for price, beauty in items:
            best = max(best, beauty)
            prices.append(price)
            prefix_beauty.append(best)

        answer = []
        for query in queries:
            index = bisect_right(prices, query) - 1
            answer.append(prefix_beauty[index] if index >= 0 else 0)
        return answer
