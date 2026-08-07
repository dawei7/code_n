from collections import defaultdict
from typing import List


class OrderManagementSystem:
    def __init__(self):
        self.orders = {}
        self.orders_at_price = defaultdict(set)

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.orders[orderId] = (orderType, price)
        self.orders_at_price[(orderType, price)].add(orderId)

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        order_type, old_price = self.orders[orderId]
        if old_price == newPrice:
            return

        old_bucket = self.orders_at_price[(order_type, old_price)]
        old_bucket.remove(orderId)
        if not old_bucket:
            del self.orders_at_price[(order_type, old_price)]

        self.orders[orderId] = (order_type, newPrice)
        self.orders_at_price[(order_type, newPrice)].add(orderId)

    def cancelOrder(self, orderId: int) -> None:
        order_type, price = self.orders.pop(orderId)
        bucket = self.orders_at_price[(order_type, price)]
        bucket.remove(orderId)
        if not bucket:
            del self.orders_at_price[(order_type, price)]

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return list(self.orders_at_price.get((orderType, price), ()))
