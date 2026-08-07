### 1. Description

You are asked to design a simple order management system for a trading platform.

Each order is associated with an `orderId`, an `orderType` (`"buy"` or `"sell"`), and a `price`.

An order is considered **active** unless it is canceled.

Implement the `OrderManagementSystem` class:

- `OrderManagementSystem()`: Initializes the order management system.

- `void addOrder(int orderId, string orderType, int price)`: Adds a new **active** order with the given attributes. It is **guaranteed** that `orderId` is unique.

- `void modifyOrder(int orderId, int newPrice)`: Modifies the **price** of an existing order. It is **guaranteed** that the order exists and is *active*.

- `void cancelOrder(int orderId)`: Cancels an existing order. It is **guaranteed** that the order exists and is *active*.

- `vector<int> getOrdersAtPrice(string orderType, int price)`: Returns the `orderId`s of all **active** orders that match the given `orderType` and `price`. If no such orders exist, return an empty list.

### 2. Function Contract

**Inputs**

- `operations`: A list that begins with `"OrderManagementSystem"` and then contains method names from `"addOrder"`, `"modifyOrder"`, `"cancelOrder"`, and `"getOrdersAtPrice"`.
- `arguments`: A parallel list containing the arguments for each construction or method call.

The app adapter constructs one stateful system and applies the operations in order. Each `modifyOrder` and `cancelOrder` call refers to an order that currently exists and is active. Modification changes the price but preserves the order's original type.

Let $Q$ be the number of method calls after construction, $A$ the maximum number of simultaneously active orders, and $T$ the total number of IDs contained in all lookup results.

**Return value**

Return one result for every entry in `operations`: `null` for construction and every mutating operation, and a list of matching active IDs for each `getOrdersAtPrice` call. A lookup with no matches contributes an empty list.

### 3. Note

The order of returned `orderId`s does not matter.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:**

["OrderManagementSystem", "addOrder", "addOrder", "addOrder", "getOrdersAtPrice", "modifyOrder", "modifyOrder", "getOrdersAtPrice", "cancelOrder", "cancelOrder", "getOrdersAtPrice"]

[[], [1, "buy", 1], [2, "buy", 1], [3, "sell", 2], ["buy", 1], [1, 3], [2, 1], ["buy", 1], [3], [2], ["buy", 1]]

**Output:**

[null, null, null, null, [2, 1], null, null, [2], null, null, []]

**Explanation**

OrderManagementSystem orderManagementSystem = new OrderManagementSystem();

orderManagementSystem.addOrder(1, "buy", 1); // A buy order with ID 1 is added at price 1.

orderManagementSystem.addOrder(2, "buy", 1); // A buy order with ID 2 is added at price 1.

orderManagementSystem.addOrder(3, "sell", 2); // A sell order with ID 3 is added at price 2.

orderManagementSystem.getOrdersAtPrice("buy", 1); // Both buy orders (IDs 1 and 2) are active at price 1, so the result is `[2, 1]`.

orderManagementSystem.modifyOrder(1, 3); // Order 1 is updated: its price becomes 3.

orderManagementSystem.modifyOrder(2, 1); // Order 2 is updated, but its price remains 1.

orderManagementSystem.getOrdersAtPrice("buy", 1); // Only order 2 is still an active buy order at price 1, so the result is `[2]`.

orderManagementSystem.cancelOrder(3); // The sell order with ID 3 is canceled and removed from active orders.

orderManagementSystem.cancelOrder(2); // The buy order with ID 2 is canceled and removed from active orders.

orderManagementSystem.getOrdersAtPrice("buy", 1); // There are no active buy orders left at price 1, so the result is `[]`.</div>

### 5. Constraints

- $1 \le orderId \le 2000$

- `orderId` is **unique** across all orders.

- `orderType` is either `"buy"` or `"sell"`.

- $1 \le price \le 10^{9}$

- The total number of calls to `addOrder`, `modifyOrder`, `cancelOrder`, and `getOrdersAtPrice` does not exceed 2000.

- For `modifyOrder` and `cancelOrder`, the specified `orderId` is **guaranteed** to exist and be *active*.