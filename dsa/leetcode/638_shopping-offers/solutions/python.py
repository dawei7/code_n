from functools import cache


def solve(price: list[int], special: list[list[int]], needs: list[int]) -> int:
    item_count = len(price)
    useful_offers = [
        offer
        for offer in special
        if any(offer[:item_count])
        and offer[-1] < sum(quantity * unit for quantity, unit in zip(offer, price))
    ]

    @cache
    def minimum_cost(remaining: tuple[int, ...]) -> int:
        best = sum(quantity * unit for quantity, unit in zip(remaining, price))
        for offer in useful_offers:
            if all(offer[index] <= remaining[index] for index in range(item_count)):
                next_remaining = tuple(
                    remaining[index] - offer[index] for index in range(item_count)
                )
                best = min(best, offer[-1] + minimum_cost(next_remaining))
        return best

    return minimum_cost(tuple(needs))
