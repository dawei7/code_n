from collections import Counter
from typing import List


class Solution:
    def score(self, cards: List[str], x: str) -> int:
        first = Counter()
        second = Counter()
        centers = 0

        for card in cards:
            if card[0] == x and card[1] == x:
                centers += 1
            elif card[0] == x:
                first[card[1]] += 1
            elif card[1] == x:
                second[card[0]] += 1

        def side_score(counts: Counter[str], allocated: int) -> int:
            side_total = sum(counts.values())
            total = side_total + allocated
            largest = max([allocated, *counts.values()])
            return min(total // 2, total - largest)

        return max(
            side_score(first, allocated) + side_score(second, centers - allocated) for allocated in range(centers + 1)
        )
