# Odd and Even Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3220 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/odd-and-even-transactions/) |

## Problem Description

### Goal

The `transactions` table records a unique transaction identifier, an integer `amount`, and its `transaction_date`. Produce one result row for every date present in the table.

For each date, sum the odd amounts into `odd_sum` and the even amounts into `even_sum`. If a date has no amount of one parity, report `0` for that sum rather than `NULL`. Return the rows in ascending `transaction_date` order.

### Function Contract

**Inputs**

- `transactions(transaction_id, amount, transaction_date)`: Transaction rows keyed by `transaction_id`; `amount` is an integer and `transaction_date` is a date.

Let $r$ be the number of input rows and $d$ the number of distinct transaction dates.

**Return value**

Return columns `transaction_date`, `odd_sum`, and `even_sum`, with one row per date ordered ascending.

### Examples

#### Example 1

- **Input:** transactions `(150, 2024-07-01)`, `(200, 2024-07-01)`, `(75, 2024-07-01)`, `(300, 2024-07-02)`, `(50, 2024-07-02)`, `(120, 2024-07-03)`
- **Output:** `(2024-07-01, 75, 350)`, `(2024-07-02, 0, 350)`, `(2024-07-03, 0, 120)`

#### Example 2

- **Input:** one transaction with amount `9` on `2024-01-01`
- **Output:** `(2024-01-01, 9, 0)`

#### Example 3

- **Input:** amounts `2`, `4`, and `6` on one date
- **Output:** that date with `odd_sum = 0` and `even_sum = 12`
