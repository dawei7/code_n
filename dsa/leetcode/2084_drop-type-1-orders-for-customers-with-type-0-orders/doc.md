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

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Summarize each customer's available types**

Compute `MIN(order_type)` as a window aggregate partitioned by `customer_id`. Because the only possible types are 0 and 1, a partition minimum of 0 proves that the customer has at least one preferred type 0 order. A minimum of 1 proves that every order in the partition is type 1.

**Retain rows matching the partition priority**

The window value is attached to every original row without collapsing the partition. Filter to rows where `order_type = minimum_type`. For a customer whose minimum is 0 this keeps every type 0 row and removes every type 1 row; when the minimum is 1 it keeps all rows. These are exactly the two contract branches.

**Project only the original columns**

The computed minimum is internal evidence and must not appear in the result. Select `order_id`, `customer_id`, and `order_type` from the filtered relation. Since the problem permits any order, no final `ORDER BY` is required.

#### Complexity detail

A typical window implementation groups or sorts the $N$ rows by customer, taking $O(N\log N)$ time and $O(N)$ execution space. Hash-partitioned execution may be linear expected time. The exact physical plan is database-dependent, while the logical query processes each original row once after its customer minimum is known.

#### Alternatives and edge cases

- **Precompute type 0 customers:** A subquery of distinct customers with type 0, followed by an anti-join for type 1 rows, expresses the same rule without a window.
- **Correlated `NOT EXISTS`:** Keep every type 0 row or a type 1 row whose customer has no type 0 row. It is correct, but an unoptimized plan can rescan `Orders` for every outer row and take $O(N^2)$ time.
- **Group and join back:** Computing `MIN(order_type)` per customer and joining to the original table is equivalent but requires an explicit second relation step.
- **Several type 0 orders:** Retain all of them, not just one representative.
- **Only type 1 orders:** Retain every order for that customer.
- **Mixed customers:** The priority decision is independent for each `customer_id`.

</details>
