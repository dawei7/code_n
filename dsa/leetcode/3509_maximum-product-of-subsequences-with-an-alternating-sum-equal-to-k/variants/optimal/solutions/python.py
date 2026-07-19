from collections import defaultdict


def solve(nums: list[int], k: int, limit: int) -> int:
    if abs(k) > sum(nums):
        return -1

    over_limit = limit + 1
    states: list[dict[int, set[int]]] = [defaultdict(set), defaultdict(set)]

    for value in nums:
        updated: list[dict[int, set[int]]] = [
            defaultdict(set, {total: set(products) for total, products in states[0].items()}),
            defaultdict(set, {total: set(products) for total, products in states[1].items()}),
        ]

        if value <= limit:
            updated[1][value].add(value)

        for parity in (0, 1):
            sign = 1 if parity == 0 else -1
            next_parity = 1 - parity
            for total, products in states[parity].items():
                next_total = total + sign * value
                target = updated[next_parity][next_total]
                for product in products:
                    next_product = product * value
                    target.add(next_product if next_product <= limit else over_limit)
        states = updated

    candidates = states[0].get(k, set()) | states[1].get(k, set())
    valid = [product for product in candidates if product <= limit]
    return max(valid) if valid else -1
