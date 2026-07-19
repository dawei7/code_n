from collections import Counter


def solve(nums: list[int], quantity: list[int]) -> bool:
    customers = len(quantity)
    full_mask = (1 << customers) - 1
    capacities = sorted(Counter(nums).values(), reverse=True)[:customers]

    demand = [0] * (1 << customers)
    for mask in range(1, full_mask + 1):
        lowest_bit = mask & -mask
        customer = lowest_bit.bit_length() - 1
        demand[mask] = demand[mask ^ lowest_bit] + quantity[customer]

    reachable = {0}
    for capacity in capacities:
        next_reachable = set(reachable)
        for served in reachable:
            remaining = full_mask ^ served
            subset = remaining
            while subset:
                if demand[subset] <= capacity:
                    next_reachable.add(served | subset)
                subset = (subset - 1) & remaining
        if full_mask in next_reachable:
            return True
        reachable = next_reachable

    return False
