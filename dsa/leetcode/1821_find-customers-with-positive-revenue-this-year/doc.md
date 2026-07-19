# Find Customers With Positive Revenue this Year

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/) |
| Frontend ID | 1821 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Customers` table stores one customer's revenue for a particular calendar year. Revenue is allowed to be positive, zero, or negative, and the same customer may have separate rows for different years.

Report the identifiers of customers whose revenue in the year 2021 is strictly greater than zero. A positive value from another year does not qualify, while zero or a negative 2021 value must be excluded. The result may be returned in any order.

### Function Contract

**Inputs**

- `Customers(customer_id, year, revenue)`: one row per `(customer_id, year)` pair.
- `customer_id` identifies a customer, `year` identifies the calendar year, and `revenue` is that customer's possibly non-positive revenue for the year.
- Let $r$ be the number of rows in `Customers`, and let $o$ be the number of qualifying output rows.

**Return value**

- Return one column named `customer_id`, containing exactly those customers whose row has `year = 2021` and `revenue > 0`.
- Result row order is not significant.

### Examples

**Example 1**

`Customers`

| customer_id | year | revenue |
|---:|---:|---:|
| 1 | 2018 | 50 |
| 1 | 2021 | 30 |
| 1 | 2020 | 70 |
| 2 | 2021 | -50 |
| 3 | 2018 | 10 |
| 3 | 2016 | 50 |
| 4 | 2021 | 20 |

Output:

| customer_id |
|---:|
| 1 |
| 4 |

Customers 1 and 4 have positive 2021 revenue. Customer 2 has a 2021 row but its revenue is negative, and customer 3 has no row for 2021.
