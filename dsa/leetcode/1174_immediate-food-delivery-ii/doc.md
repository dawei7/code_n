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
