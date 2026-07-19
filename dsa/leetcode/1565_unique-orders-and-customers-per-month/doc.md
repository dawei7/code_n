# Unique Orders and Customers Per Month

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1565 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-orders-and-customers-per-month/) |

## Problem Description
### Goal

The `Orders` table records each order's unique identifier, date, customer, and invoice amount. Consider only orders whose invoice is strictly greater than `20`.

For every calendar month containing at least one qualifying order, report the month in `YYYY-MM` form, the number of qualifying orders, and the number of distinct customers who placed those orders. Months with no qualifying orders do not appear. The rows may be returned in any order.

### Function Contract
**Inputs**

- `Orders(order_id, order_date, customer_id, invoice)`: a table of $r$ orders. `order_id` is unique, `order_date` is a date, and `invoice` is an integer amount.

**Return value**

Return a table with columns `month`, `order_count`, and `customer_count`. Each row represents one year-month among orders with `invoice > 20`; `order_count` counts its qualifying orders and `customer_count` counts its distinct qualifying customers.

### Examples
**Example 1**

- Input: qualifying orders in September, October, and December 2020 and January 2021, together with invoices of `20` or less
- Output: `(2020-09, 2, 2)`, `(2020-10, 1, 1)`, `(2020-12, 2, 1)`, and `(2021-01, 1, 1)`
- Explanation: invoices equal to `20` are excluded, and the two December orders belong to one customer.

**Example 2**

- Input: three qualifying orders from one customer in the same month
- Output: one row with `order_count = 3` and `customer_count = 1`

**Example 3**

- Input: only orders whose invoices are at most `20`
- Output: an empty result
