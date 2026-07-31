## Description

Design a simple order-management system for a trading platform.

Every order has an `orderId`, an `orderType` whose value is either `"buy"` or `"sell"`, and a `price`. An order remains **active** from the time it is added until it is canceled.

Implement the `OrderManagementSystem` class with these operations:

- `OrderManagementSystem()` creates an empty system.
- `addOrder(orderId, orderType, price)` adds a new active order with those attributes. The supplied `orderId` is guaranteed to be unique.
- `modifyOrder(orderId, newPrice)` changes only the price of an existing active order to `newPrice`.
- `cancelOrder(orderId)` cancels an existing active order, so it must no longer appear in lookups.
- `getOrdersAtPrice(orderType, price)` returns every active order ID whose type and price both equal the requested values. Return an empty list when there is no match.
