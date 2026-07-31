from collections import defaultdict


class OrderManagementSystem:
    def __init__(self) -> None:
        self.orders: dict[int, tuple[str, int]] = {}
        self.orders_at_price: defaultdict[tuple[str, int], set[int]] = defaultdict(set)

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

    def getOrdersAtPrice(self, orderType: str, price: int) -> list[int]:
        return list(self.orders_at_price.get((orderType, price), ()))


def solve(operations: list[str], arguments: list[list[int | str]]) -> list[list[int] | None]:
    system: OrderManagementSystem | None = None
    results: list[list[int] | None] = []

    for operation, values in zip(operations, arguments, strict=True):
        if operation == "OrderManagementSystem":
            system = OrderManagementSystem()
            results.append(None)
        elif operation == "addOrder":
            assert system is not None
            system.addOrder(int(values[0]), str(values[1]), int(values[2]))
            results.append(None)
        elif operation == "modifyOrder":
            assert system is not None
            system.modifyOrder(int(values[0]), int(values[1]))
            results.append(None)
        elif operation == "cancelOrder":
            assert system is not None
            system.cancelOrder(int(values[0]))
            results.append(None)
        elif operation == "getOrdersAtPrice":
            assert system is not None
            results.append(system.getOrdersAtPrice(str(values[0]), int(values[1])))
        else:
            raise ValueError(f"unknown operation: {operation}")

    return results
