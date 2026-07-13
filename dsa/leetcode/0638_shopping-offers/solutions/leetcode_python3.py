from functools import lru_cache
from typing import List


class Solution:
    def shoppingOffers(
        self,
        price: List[int],
        special: List[List[int]],
        needs: List[int],
    ) -> int:
        item_count = len(price)
        useful_offers = [
            offer
            for offer in special
            if any(offer[:item_count])
            and offer[-1] < sum(quantity * unit for quantity, unit in zip(offer, price))
        ]

        @lru_cache(None)
        def minimum_cost(remaining):
            best = sum(quantity * unit for quantity, unit in zip(remaining, price))
            for offer in useful_offers:
                if all(offer[index] <= remaining[index] for index in range(item_count)):
                    next_remaining = tuple(
                        remaining[index] - offer[index] for index in range(item_count)
                    )
                    best = min(best, offer[-1] + minimum_cost(next_remaining))
            return best

        return minimum_cost(tuple(needs))
