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

### Required Complexity

- **Time:** $O(r\log r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Partition by the calendar date**

Use `DATE(day)` as the window partition key. This removes the time component without merging equal day-of-month numbers from different months or years. Every transaction on the same full calendar date is therefore compared within one group.

**Rank amounts while preserving ties**

Within each date partition, order `amount` descending and apply `RANK()`. Every row with the maximum amount receives rank 1. Unlike `ROW_NUMBER()`, `RANK()` assigns the same rank to equal amounts, so filtering for rank 1 returns all daily co-maxima.

The common table expression retains each `transaction_id` beside its rank. The outer query filters to rank 1 and orders the surviving IDs numerically in ascending order, independently of date and input order.

**Why the filter returns exactly the required rows**

For a fixed date, descending amount order places no value ahead of a maximum, so each maximum row has rank 1. Any smaller amount has at least one maximum before it and receives a rank greater than 1. The filter therefore includes all and only maximum transactions in every partition; the final sort then satisfies the output-order contract.

#### Complexity detail

For $r$ rows, partitioned ordering takes $O(r\log r)$ time in the general case, followed by a linear filter and result sort bounded by the same order. The window ranking and sort may retain $O(r)$ rows of working state.

#### Alternatives and edge cases

- **Aggregate and join:** Compute `MAX(amount)` per `DATE(day)` and join it back to `Transactions`; this is correct and naturally preserves ties, but it performs a separate aggregation and matching step.
- **Correlated `NOT EXISTS`:** Select a transaction only when no larger amount exists on its date; without suitable indexing this can compare quadratically many row pairs.
- **`ROW_NUMBER()`:** It incorrectly discards all but one transaction when several IDs tie for the daily maximum.
- **Day-of-month extraction:** Grouping only by `DAY(day)` incorrectly merges dates from different months or years; use the complete calendar date.
- **Different times on one date:** Time-of-day does not split the daily partition.
- **Midnight boundary:** Timestamps immediately before and after midnight belong to different dates.
- **Tied maxima:** Every tied ID must appear once.
- **Single transaction date:** Its only row receives rank 1.
- **Output ordering:** Sort by ID, not by date, amount, rank, or insertion order.

</details>
