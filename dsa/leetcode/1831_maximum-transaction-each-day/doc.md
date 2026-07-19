# Maximum Transaction Each Day

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-transaction-each-day/) |
| Frontend ID | 1831 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Transactions` table records a unique transaction identifier, its date and time, and its amount. Transactions at different times on the same calendar date belong to the same daily group.

Report the identifier of every transaction whose amount is the maximum for its calendar date. When several transactions tie for that daily maximum, include all of them. Sort the result by `transaction_id` in ascending order.

### Function Contract

**Inputs**

- `Transactions(transaction_id, day, amount)`:
  - `transaction_id` is a unique integer.
  - `day` is the transaction date and time.
  - `amount` is the transaction's integer amount.
- Let $r$ be the number of rows in `Transactions`.

**Return value**

- Return one column named `transaction_id`.
- Include exactly those IDs whose amount equals the maximum amount among transactions on the same calendar date.
- Order the rows by `transaction_id` ascending.

### Examples

**Example 1**

`Transactions`

| transaction_id | day | amount |
|---:|---|---:|
| 8 | `2021-04-03 15:57:28` | 57 |
| 9 | `2021-04-28 08:47:25` | 21 |
| 1 | `2021-04-29 13:28:30` | 58 |
| 5 | `2021-04-28 16:39:59` | 40 |
| 6 | `2021-04-29 23:39:28` | 58 |

Output:

| transaction_id |
|---:|
| 1 |
| 5 |
| 6 |
| 8 |

IDs 1 and 6 tie on April 29, while ID 5 exceeds ID 9 on April 28.

**Example 2**

For rows `(4, 2022-01-01 23:59:59, 10)` and `(2, 2022-01-02 00:00:00, 5)`, both IDs are returned because the timestamps fall on different calendar dates.

**Example 3**

If a date contains only one transaction, that transaction is necessarily its day's maximum.
