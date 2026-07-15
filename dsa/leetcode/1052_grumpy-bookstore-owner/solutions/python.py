"""Optimal solution for LeetCode 1052: Grumpy Bookstore Owner."""


def solve(customers: list[int], grumpy: list[int], minutes: int) -> int:
    baseline = sum(
        customer
        for customer, is_grumpy in zip(customers, grumpy)
        if not is_grumpy
    )

    window_gain = 0
    best_gain = 0
    for index, (customer, is_grumpy) in enumerate(zip(customers, grumpy)):
        if is_grumpy:
            window_gain += customer
        if index >= minutes and grumpy[index - minutes]:
            window_gain -= customers[index - minutes]
        best_gain = max(best_gain, window_gain)

    return baseline + best_gain
