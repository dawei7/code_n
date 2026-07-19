# Monthly Transactions I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1193 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/monthly-transactions-i/) |

## Problem Description

### Goal

The `Transactions` table records incoming transactions. Each row has a unique transaction `id`, a `country`, a `state` that is either `"approved"` or `"declined"`, an integer `amount`, and the calendar date `trans_date` on which the transaction occurred.

For every distinct calendar month and country combination, report the number and total amount of all transactions, together with the number and total amount of only the approved transactions. Represent the month in `YYYY-MM` form and return the result rows in any order.

### Function Contract

**Input table**

- `Transactions(id, country, state, amount, trans_date)`: `id` is the primary key, `state` is either `"approved"` or `"declined"`, and `trans_date` is a date.
- Let $n$ be the number of transaction rows and $g$ the number of distinct `(month, country)` groups.

**Return value**

- One row per month-country group with columns `month`, `country`, `trans_count`, `approved_count`, `trans_total_amount`, and `approved_total_amount`.
- `month` uses the `YYYY-MM` representation derived from `trans_date`.

### Examples

**Example 1**

`Transactions`

| id | country | state | amount | trans_date |
|---:|---|---|---:|---|
| 121 | US | approved | 1000 | 2018-12-18 |
| 122 | US | declined | 2000 | 2018-12-19 |
| 123 | US | approved | 2000 | 2019-01-01 |
| 124 | DE | approved | 2000 | 2019-01-07 |

Output:

| month | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
|---|---|---:|---:|---:|---:|
| 2018-12 | US | 2 | 1 | 3000 | 1000 |
| 2019-01 | DE | 1 | 1 | 2000 | 2000 |
| 2019-01 | US | 1 | 1 | 2000 | 2000 |

**Example 2**

A group containing only declined transactions still appears with `approved_count = 0` and `approved_total_amount = 0`.

**Example 3**

Transactions from the same country in different calendar months belong to separate result rows.
