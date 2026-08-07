from collections import Counter
from typing import List


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        kept = Counter(candies[k:])
        answer = len(kept)

        for right in range(k, len(candies)):
            kept[candies[right - k]] += 1

            entering_shared = candies[right]
            kept[entering_shared] -= 1
            if kept[entering_shared] == 0:
                del kept[entering_shared]

            answer = max(answer, len(kept))

        return answer
