# Immediate Food Delivery I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1173 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/immediate-food-delivery-i/) |

## Problem Description

### Goal

The `Delivery` table records food orders. Each customer places an order on `order_date` and chooses a `customer_pref_delivery_date` that is either the same date or a later date. An order is called immediate when these two dates are equal; otherwise, it is called scheduled.

Find the percentage of all orders that are immediate. Return one row with the result rounded to two decimal places and named `immediate_percentage`.

### Function Contract

**Input table**

- `Delivery(delivery_id, customer_id, order_date, customer_pref_delivery_date)`: `delivery_id` is the primary key. Each row describes one order, its customer, its order date, and its preferred delivery date.
- Let $n$ be the number of rows in `Delivery`.

**Return value**

- One row and one column named `immediate_percentage`, containing the immediate-order count divided by the total order count, multiplied by $100$ and rounded to two decimal places.

### Examples

**Example 1**

`Delivery`

| delivery_id | customer_id | order_date | customer_pref_delivery_date |
|---:|---:|---|---|
| 1 | 1 | 2019-08-01 | 2019-08-02 |
| 2 | 5 | 2019-08-02 | 2019-08-02 |
| 3 | 1 | 2019-08-11 | 2019-08-11 |
| 4 | 3 | 2019-08-24 | 2019-08-26 |
| 5 | 4 | 2019-08-21 | 2019-08-22 |
| 6 | 2 | 2019-08-11 | 2019-08-13 |

Output:

| immediate_percentage |
|---:|
| 33.33 |

Orders `2` and `3` are immediate, so the percentage is $100\times 2/6=33.33$ after rounding.

**Example 2**

If every row has matching order and preferred dates, the result is `100.00`.

**Example 3**

If none of the dates match, the result is `0.00`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Turn the classification into a numeric contribution.** A `CASE` expression emits `1.0` when `order_date = customer_pref_delivery_date` and `0.0` otherwise. Each row therefore contributes exactly the indicator for being immediate.

**Aggregate the ratio directly.** The average of these zero-or-one indicators is the fraction of immediate orders. Multiplying that average by `100.0` converts it to a percentage, and `ROUND(..., 2)` supplies the required precision. Using decimal literals avoids accidental integer division in database engines where dividing integers would truncate.

Because the query has no `GROUP BY`, the aggregate produces exactly one output row. Aliasing the expression as `immediate_percentage` establishes the required column name.

#### Complexity detail

The aggregate examines each of the $n$ delivery rows once, so its logical running time is $O(n)$. Apart from the aggregate's counters, it needs $O(1)$ working space; physical execution details remain database-engine dependent.

#### Alternatives and edge cases

- **Conditional `SUM` divided by `COUNT`:** This is equally valid and has the same $O(n)$ logical cost, provided the division is forced to use a non-integer numeric type.
- **Filter and count in a subquery:** Counting immediate rows separately and dividing by another total count is correct but may require two scans instead of one.
- **All immediate orders:** The indicator average is `1`, producing `100.00`.
- **No immediate orders:** The indicator average is `0`, producing `0.00`.
- **Repeated customer:** Classification is per delivery row, not per distinct customer.
- **Scheduled boundary:** Any preferred date later than the order date is scheduled; only exact equality is immediate.

</details>
