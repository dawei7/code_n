"""Optimal app-local solution for LeetCode 901."""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, previous_span = self.stack.pop()
            span += previous_span
        self.stack.append((price, span))
        return span


def solve(operations):
    spanner = StockSpanner()
    return [spanner.next(operation[1]) for operation in operations]
