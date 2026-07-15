from typing import List


class Cashier:
    def __init__(
        self, n: int, discount: int, products: List[int], prices: List[int]
    ):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        self.price_by_product = dict(zip(products, prices))

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        total = sum(
            self.price_by_product[item] * quantity
            for item, quantity in zip(product, amount)
        )
        if self.customer_count % self.n == 0:
            total *= (100 - self.discount) / 100
        return float(total)
