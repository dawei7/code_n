## Examples

**Example 1**

- Input: `operations = ["OrderManagementSystem", "addOrder", "addOrder", "addOrder", "getOrdersAtPrice", "modifyOrder", "modifyOrder", "getOrdersAtPrice", "cancelOrder", "cancelOrder", "getOrdersAtPrice"]; arguments = [[], [1, "buy", 1], [2, "buy", 1], [3, "sell", 2], ["buy", 1], [1, 3], [2, 1], ["buy", 1], [3], [2], ["buy", 1]]`
- Output: `[null, null, null, null, [2, 1], null, null, [2], null, null, []]`
- Explanation:
  - `OrderManagementSystem orderManagementSystem = new OrderManagementSystem();` initializes the system.
  - `orderManagementSystem.addOrder(1, "buy", 1);` adds buy order `1` at price `1`.
  - `orderManagementSystem.addOrder(2, "buy", 1);` adds buy order `2` at price `1`.
  - `orderManagementSystem.addOrder(3, "sell", 2);` adds sell order `3` at price `2`.
  - `orderManagementSystem.getOrdersAtPrice("buy", 1);` finds both active buy orders at price `1`, so `[2, 1]` is a valid result.
  - `orderManagementSystem.modifyOrder(1, 3);` changes order `1`'s price to `3`.
  - `orderManagementSystem.modifyOrder(2, 1);` modifies order `2`, but its price remains `1`.
  - `orderManagementSystem.getOrdersAtPrice("buy", 1);` now finds only order `2`, producing `[2]`.
  - `orderManagementSystem.cancelOrder(3);` cancels sell order `3` and removes it from the active set.
  - `orderManagementSystem.cancelOrder(2);` cancels buy order `2` and removes it from the active set.
  - `orderManagementSystem.getOrdersAtPrice("buy", 1);` finds no remaining active buy order at price `1`, producing `[]`.
