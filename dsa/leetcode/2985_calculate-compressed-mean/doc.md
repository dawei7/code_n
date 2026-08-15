# Calculate Compressed Mean

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2985 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-compressed-mean/) |

## Problem Description

### Goal

The `Orders` table stores a compressed distribution of order sizes. Each
unique `order_id` row says that an order containing `item_count` items occurs
`order_occurrences` times; the row therefore represents that many individual
orders rather than one order.

Calculate the average number of items per represented order and round it to
two decimal places. Return the single value under the column name
`average_items_per_order`; row ordering is irrelevant because the result has
one row.

### Function Contract

**Inputs**

- `Orders(order_id, item_count, order_occurrences)`: compressed order-size frequencies with unique `order_id` values

Let $R$ be the number of compressed rows.

**Return value**

Return one row containing the occurrence-weighted mean, rounded to two decimal
places, as `average_items_per_order`.

### Examples

#### Example 1

- **Input:** `(item_count, order_occurrences)` values `(1,500)`, `(2,1000)`, `(3,800)`, and `(4,1000)`
- **Output:** `2.70`
- **Explanation:** The represented item total is `8900`, the order total is `3300`, and their quotient rounds to `2.70`.

#### Example 2

- **Input:** One row representing `999` orders with `7` items each
- **Output:** `7.00`

#### Example 3

- **Input:** One one-item order and two two-item orders
- **Output:** `1.67`
