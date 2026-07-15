# Customers Who Bought Products A and B but Not C

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1398 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/) |

## Problem Description

### Goal

The `Customers` table identifies each customer and gives their name. The `Orders` table records product purchases and associates each order with a customer.

Find customers who have purchased product `"A"` at least once and product `"B"` at least once, but have never purchased product `"C"`. Other product purchases do not disqualify a customer. Return each qualifying customer's identifier and name, ordered by customer identifier.

### Function Contract

**Inputs**

- `Customers(customer_id, customer_name)`: $C$ customer rows.
- `Orders(order_id, customer_id, product_name)`: $O$ purchase rows.

Let $R$ be the number of qualifying customers.

**Return value**

- A relation with columns `customer_id` and `customer_name`, containing the $R$ customers who bought both A and B and never C, ordered by `customer_id`.

### Examples

**Example 1**

- Input: customer `1` has orders for A and B.
- Output: that customer's identifier and name.

**Example 2**

- Input: customer `2` has orders for A, B, and C.
- Output: no row for customer `2`.

**Example 3**

- Input: customer `3` has repeated A orders and one B order, plus product D.
- Output: customer `3` still qualifies.

### Required Complexity

- **Time:** $O(C + O + R)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

Join customers to their orders and group by customer. Within each group, use conditional sums to count purchases of A, B, and C. Keep the group only when the A count and B count are positive and the C count is zero.

Every joined row belongs to its purchasing customer, so each conditional aggregate examines exactly that customer's orders. The three `HAVING` conditions are therefore equivalent to the required existential A condition, existential B condition, and universal absence-of-C condition. Purchases of any other product contribute zero to all three counts and do not affect qualification.

An inner join naturally omits customers without orders; they cannot have bought both required products. Order the surviving rows by customer identifier.

#### Complexity detail

With indexed or hash joining and hash aggregation, reading $C$ customers and $O$ orders and emitting $R$ results takes $O(C + O + R)$ time. Grouping and join state use $O(C)$ space. A sort-based physical plan may add database-specific sorting costs.

#### Alternatives and edge cases

- **Three correlated subqueries:** Separate `EXISTS` checks for A and B plus `NOT EXISTS` for C are clear but can rescan all orders per customer, costing $O(CO)$ without useful indexes.
- **Self-join order aliases:** Join A and B orders and anti-join C orders. Repeated purchases can multiply intermediate rows unless carefully deduplicated.
- **Repeated purchases:** One or many A or B orders satisfy the same presence requirement.
- **Product C:** A single C order disqualifies the customer regardless of other purchases.
- **Other products:** They neither qualify nor disqualify a customer.
- **Missing required product:** Buying only A or only B is insufficient.
- **No orders:** Such a customer cannot appear in the result.

</details>
