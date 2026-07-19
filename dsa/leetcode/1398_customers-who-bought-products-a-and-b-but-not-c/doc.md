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
