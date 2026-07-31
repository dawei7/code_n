"""App-local adapter and reference design for LeetCode 1352."""


class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num):
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]


def solve(operations):
    product = ProductOfNumbers()
    output = []
    for operation, arguments in operations:
        if operation == "add":
            product.add(*arguments)
            output.append(None)
        elif operation == "getProduct":
            output.append(product.getProduct(*arguments))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
