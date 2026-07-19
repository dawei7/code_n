# Drop Type 1 Orders for Customers With Type 0 Orders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2084 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/) |

## Problem Description

### Goal

The `Orders` table records orders with a unique order identifier, a customer identifier, and an order type that is either 0 or 1.

Report orders customer by customer under one priority rule. If a customer has at least one type 0 order, retain all of that customer's type 0 orders and discard every type 1 order from that customer. If the customer has no type 0 order, retain all of their type 1 orders. Return the selected original rows in any order.

### Function Contract

**Inputs**

- `Orders(order_id, customer_id, order_type)`: a relation of $N$ orders where `order_id` is unique and every `order_type` is either 0 or 1.

**Return value**

- Return the selected `order_id`, `customer_id`, and `order_type` columns for every row that survives its customer's type-priority rule. Output order is unrestricted.

### Examples

**Example 1**

- Input: `Orders = [[1,1,0],[2,1,0],[11,2,0],[12,2,1],[21,3,1],[22,3,0],[31,4,1],[32,4,1]]`
- Output: `[[1,1,0],[2,1,0],[11,2,0],[22,3,0],[31,4,1],[32,4,1]]`
- Explanation: Customers 1, 2, and 3 have type 0 orders, while customer 4 has only type 1 orders.

**Example 2**

- Input: `Orders = [[5,7,1],[6,7,1]]`
- Output: `[[5,7,1],[6,7,1]]`
- Explanation: With no type 0 order for customer 7, both type 1 rows remain.

**Example 3**

- Input: `Orders = [[8,2,1],[9,2,0],[10,2,0]]`
- Output: `[[9,2,0],[10,2,0]]`
- Explanation: The presence of either type 0 row suppresses the customer's type 1 row but not the other type 0 rows.
