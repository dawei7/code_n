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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(g)$

<details>
<summary>Approach</summary>

#### General

**Form the reporting key.** Extract the year and month from `trans_date` in `YYYY-MM` form, then group by that expression together with `country`. This creates exactly one aggregate group for each requested month-country combination; dates from different days of the same month contribute together.

**Compute totals and approved subsets together.** `COUNT(*)` and `SUM(amount)` cover every row in a group. Conditional aggregates contribute `1` and `amount` only when `state = 'approved'`, using zero otherwise. A group with no approved rows consequently produces numeric zeros rather than `NULL`, while declined transactions still contribute to the two overall totals.

**Keep local output deterministic.** The problem permits any result order. The app-local query adds `ORDER BY month, country` so authored fixtures produce stable rows, while the native MySQL query may use the same harmless ordering.

#### Complexity detail

With hash aggregation, the database scans the $n$ transaction rows once and performs constant work for each row, giving $O(n)$ logical time. The grouping state holds six fixed aggregates or keys for each of the $g$ month-country groups, requiring $O(g)$ auxiliary space. A database engine may instead choose a sort-based physical plan with different constants or sorting costs.

#### Alternatives and edge cases

- **Correlated subqueries per group:** Recomputing each count and sum by rescanning `Transactions` for every distinct group is correct but can require $O(gn)$ time.
- **Separate approved and total aggregations:** Two grouped queries joined on month and country work, but scan or aggregate the source twice and require care for groups with no approved rows.
- **Declined-only group:** Conditional expressions must use zero so approved aggregates return `0`, not `NULL`.
- **Month boundary:** Transactions on the last day of one month and first day of the next belong to different groups even when their country matches.
- **Country separation:** Equal months from different countries must not be combined.
- **Zero amount:** A zero-valued approved transaction increases both transaction counts while adding zero to both amounts.
- **Row order:** Input ordering has no effect on grouping, and output ordering is not part of the platform contract.

</details>
