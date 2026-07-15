"""App-local adapter and reference design for LeetCode 1357."""


class Cashier:
    def __init__(self, n, discount, products, prices):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        self.price_by_product = dict(zip(products, prices))

    def getBill(self, product, amount):
        self.customer_count += 1
        total = sum(
            self.price_by_product[item] * quantity
            for item, quantity in zip(product, amount)
        )
        if self.customer_count % self.n == 0:
            total *= (100 - self.discount) / 100
        return float(total)


def solve(n, discount, products, prices, orders):
    cashier = Cashier(n, discount, products, prices)
    return [cashier.getBill(product, amount) for product, amount in orders]
