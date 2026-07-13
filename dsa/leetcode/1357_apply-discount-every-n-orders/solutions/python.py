class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        self.price_by_product = dict(zip(products, prices))

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.customer_count += 1
        total = sum(self.price_by_product[item] * count for item, count in zip(product, amount))
        if self.customer_count % self.n == 0:
            total *= (100 - self.discount) / 100
        return float(total)


def solve(
    n: int,
    discount: int,
    products: list[int],
    prices: list[int],
    orders: list[tuple[list[int], list[int]]],
) -> list[float]:
    cashier = Cashier(n, discount, products, prices)
    return [cashier.getBill(product, amount) for product, amount in orders]
