from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if all(suit == suits[0] for suit in suits):
            return "Flush"

        counts = [0] * 14
        for rank in ranks:
            counts[rank] += 1

        largest = max(counts)
        if largest >= 3:
            return "Three of a Kind"
        if largest == 2:
            return "Pair"
        return "High Card"
