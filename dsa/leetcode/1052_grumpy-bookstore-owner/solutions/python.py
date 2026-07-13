"""Optimal solution for LeetCode 1052: Grumpy Bookstore Owner."""


def solve(customers: list[int], grumpy: list[int], minutes: int) -> int:
    base = sum(c for c, g in zip(customers, grumpy) if g == 0)
    extra = 0
    best_extra = 0
    for i, (customer, is_grumpy) in enumerate(zip(customers, grumpy)):
        if is_grumpy:
            extra += customer
        if i >= minutes and grumpy[i - minutes]:
            extra -= customers[i - minutes]
        best_extra = max(best_extra, extra)
    return base + best_extra
