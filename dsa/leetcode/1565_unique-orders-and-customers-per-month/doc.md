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

### Required Complexity

- **Time:** $O(r \log r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Filter before aggregating**

Apply `invoice > 20` in the `WHERE` clause. The inequality is strict: an invoice equal to `20` contributes to neither count. Filtering first also ensures that a month containing only nonqualifying orders does not create an output group.

**Use the year and month as one grouping key**

Format `order_date` as `YYYY-MM` with `DATE_FORMAT`. Including the year prevents, for example, January 2020 and January 2021 from being merged. The zero-padded representation also supplies the requested `month` value directly.

**Count rows and distinct customers separately**

Because `order_id` is unique, `COUNT(order_id)` is the number of qualifying orders in a month. Customers can place more than one order, so `COUNT(DISTINCT customer_id)` is required for `customer_count`. Grouping by the same formatted month produces exactly one row per qualifying calendar month, with both aggregates evaluated over precisely that month's filtered rows.

#### Complexity detail

For $r$ order rows, filtering is linear and a portable sort-based grouping has an $O(r \log r)$ time upper bound. A database can reduce this toward linear time with hash aggregation or a suitable index, but the query does not depend on either optimization.

The filtered and grouped working data can contain $O(r)$ rows or distinct values, so the portable auxiliary-space bound is $O(r)$.

#### Alternatives and edge cases

- **Extract year and month separately:** grouping by `YEAR(order_date)` and `MONTH(order_date)` is equivalent, but the formatted key is still needed for the output.
- **Correlated monthly subqueries:** derive each month and rescan `Orders` to compute its two counts. This is correct but can take $O(r^2)$ time when many months are present.
- **Conditional aggregation without filtering:** conditional counts can work, but grouping every input month can incorrectly retain a month whose qualifying counts are both zero unless it is removed afterward.
- Invoices equal to `20` are excluded because the predicate is strictly greater than `20`.
- Several orders from one customer increase `order_count` multiple times but `customer_count` once within that month.
- The same customer appearing in different months counts once in each relevant monthly group.
- The year is part of the group, so equal month numbers in different years remain separate.
- Months with no qualifying order are absent rather than reported with zero counts.
- Input row order has no effect on grouping, and the output order is unrestricted.

</details>
