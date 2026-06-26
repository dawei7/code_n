"""Optimal solution for LeetCode 1357: Apply Discount Every n Orders."""


def solve(
    n: int,
    discount: int,
    products: list[int],
    prices: list[int],
    orders: list[tuple[list[int], list[int]]],
) -> list[float]:
    price_by_product = dict(zip(products, prices))
    bills: list[float] = []
    for customer_count, (product, amount) in enumerate(orders, start=1):
        total = sum(price_by_product[item] * count for item, count in zip(product, amount))
        if customer_count % n == 0:
            total *= (100 - discount) / 100
        bills.append(float(total))
    return bills
