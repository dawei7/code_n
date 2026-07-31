from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index = {}
        best = len(cards) + 1
        for index, value in enumerate(cards):
            if value in last_index:
                best = min(best, index - last_index[value] + 1)
            last_index[value] = index
        return best if best <= len(cards) else -1
