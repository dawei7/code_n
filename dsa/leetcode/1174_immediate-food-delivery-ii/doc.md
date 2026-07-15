# Immediate Food Delivery II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1174 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/immediate-food-delivery-ii/) |

## Problem Description

### Goal

The `Delivery` table records food orders. A customer places an order on `order_date` and selects a `customer_pref_delivery_date` that is the same date or later. An order is immediate when the preferred date equals the order date; otherwise, it is scheduled.

For each customer, identify only that customer's first order, meaning the row with their earliest `order_date`. Find the percentage of these first orders that are immediate. Return one row with the percentage rounded to two decimal places and named `immediate_percentage`.

### Function Contract

**Input table**

- `Delivery(delivery_id, customer_id, order_date, customer_pref_delivery_date)`: `delivery_id` is the primary key, and each customer's `order_date` values are distinct. Each row describes one order and its requested delivery date.
- Let $n$ be the number of delivery rows and $c$ the number of distinct customers.

**Return value**

- One row and one column named `immediate_percentage`, containing the number of customers whose first order is immediate divided by $c$, multiplied by $100$ and rounded to two decimal places.

### Examples

**Example 1**

`Delivery`

| delivery_id | customer_id | order_date | customer_pref_delivery_date |
|---:|---:|---|---|
| 1 | 1 | 2019-08-01 | 2019-08-02 |
| 2 | 2 | 2019-08-02 | 2019-08-02 |
| 3 | 1 | 2019-08-11 | 2019-08-12 |
| 4 | 3 | 2019-08-24 | 2019-08-24 |
| 5 | 3 | 2019-08-21 | 2019-08-22 |
| 6 | 2 | 2019-08-11 | 2019-08-13 |
| 7 | 4 | 2019-08-09 | 2019-08-09 |

Output:

| immediate_percentage |
|---:|
| 50.00 |

The first orders for customers `1` and `3` are scheduled, while those for customers `2` and `4` are immediate.

**Example 2**

A later immediate order does not count when the same customer's first order was scheduled.

**Example 3**

A customer with exactly one order contributes according to that single row.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(c)$

<details>
<summary>Approach</summary>

#### General

**Find one earliest date per customer.** Group `Delivery` by `customer_id` and compute `MIN(order_date)`. The distinct-date guarantee means the pair `(customer_id, first_date)` identifies exactly one delivery row for every customer.

**Restrict the percentage to those rows.** Keep a delivery only when its `(customer_id, order_date)` pair appears in the grouped result. This prevents later orders from influencing the calculation, even when a later order has a different immediate-or-scheduled classification.

**Aggregate the retained indicators.** For each first order, a `CASE` expression contributes `1.0` when the two dates match and `0.0` otherwise. Its average is the fraction of customers whose first order is immediate. Multiply by `100.0`, round to two decimal places, and expose the required `immediate_percentage` alias.

#### Complexity detail

Logically, grouping and filtering process the $n$ delivery rows a constant number of times, for $O(n)$ time with hash aggregation. The grouped first-date relation stores one entry for each of the $c$ customers, using $O(c)$ auxiliary space. A database engine may instead choose sorting or indexed access with different physical costs.

#### Alternatives and edge cases

- **Window `ROW_NUMBER`:** Partitioning by customer and ordering by `order_date` also isolates the first row, but generally introduces an explicit sort unless a supporting index exists.
- **Correlated minimum subquery:** Comparing every row to a per-row `MIN(order_date)` is concise, but without a suitable index it can rescan the table for every delivery and take $O(n^2)$ time.
- **Later immediate order:** It must be ignored when an earlier scheduled order exists for that customer.
- **Later scheduled order:** It does not change a customer's contribution when the first order was immediate.
- **One-order customer:** That sole row is necessarily the customer's first order.
- **Repeated customers:** The denominator is the number of customers, not the total number of deliveries.

</details>
