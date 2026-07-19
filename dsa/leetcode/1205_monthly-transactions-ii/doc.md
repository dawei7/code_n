# Monthly Transactions II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1205 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/monthly-transactions-ii/) |

## Problem Description

### Goal

The `Transactions` table records incoming transactions. Each row has a unique `id`, a `country`, an `amount`, a transaction date, and a `state` that is either `"approved"` or `"declined"`.

The `Chargebacks` table records incoming chargebacks for transactions in `Transactions`; `trans_id` refers to the original transaction's `id`. A chargeback may correspond to a transaction that was declined as well as one that was approved, and its own `trans_date` may fall in a later month than the original transaction.

For every month-country combination having relevant activity, report the count and total amount of approved transactions in their transaction month, together with the count and total amount of chargebacks in their chargeback month. Omit any month-country row for which all four reported values would be zero. Return the result rows in any order.

### Function Contract

**Input tables**

- `Transactions(id, country, state, amount, trans_date)`: `id` is unique and `state` is either `"approved"` or `"declined"`.
- `Chargebacks(trans_id, trans_date)`: `trans_id` references `Transactions.id`; its date is the chargeback date.
- Let $t$ be the number of transaction rows, $c$ the number of chargeback rows, and $g$ the number of reported month-country groups.

**Return value**

- One row per relevant month-country group with columns `month`, `country`, `approved_count`, `approved_amount`, `chargeback_count`, and `chargeback_amount`.
- `month` is represented as `YYYY-MM`; approved metrics use the original transaction date, while chargeback metrics use the chargeback date.

### Examples

**Example 1**

`Transactions`

| id | country | state | amount | trans_date |
|---:|---|---|---:|---|
| 101 | US | approved | 1000 | 2019-05-18 |
| 102 | US | declined | 2000 | 2019-05-19 |
| 103 | US | approved | 3000 | 2019-06-10 |
| 104 | US | declined | 4000 | 2019-06-13 |
| 105 | US | approved | 5000 | 2019-06-15 |

`Chargebacks`

| trans_id | trans_date |
|---:|---|
| 102 | 2019-05-29 |
| 101 | 2019-06-30 |
| 105 | 2019-09-18 |

Output:

| month | country | approved_count | approved_amount | chargeback_count | chargeback_amount |
|---|---|---:|---:|---:|---:|
| 2019-05 | US | 1 | 1000 | 1 | 2000 |
| 2019-06 | US | 2 | 8000 | 1 | 1000 |
| 2019-09 | US | 0 | 0 | 1 | 5000 |

**Example 2**

A declined transaction contributes no approved metrics, but a later chargeback for it still contributes one chargeback and its full amount.

**Example 3**

A month-country pair containing only declined transactions with no chargebacks is omitted because every requested metric would be zero.
