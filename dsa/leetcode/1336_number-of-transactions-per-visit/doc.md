# Number of Transactions per Visit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1336 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-transactions-per-visit/) |

## Problem Description
### Goal
The `Visits` table records the date on which each user visited a bank. The `Transactions` table records individual transactions, including the user and transaction date. A transaction belongs to a visit only when both its user and date match that visit.

For every visit, determine how many transactions occurred during it. Then summarize how many visits had each transaction count.

The result must include every integer `transactions_count` from 0 through the largest count observed on any visit, even when no visit has a particular intermediate count. Report that absent bucket with `visits_count = 0`, and order the rows by `transactions_count` ascending.

### Function Contract
**Inputs**

- `Visits(user_id, visit_date)`: one row per user visit, uniquely identified by the user and date.
- `Transactions(user_id, transaction_date, amount)`: one row per transaction; multiple transaction rows may share the same user and date.

**Return value**

A table with columns `transactions_count` and `visits_count`, containing consecutive transaction-count buckets from 0 through the maximum observed count in ascending order.

Let $V$ and $T$ be the numbers of rows in `Visits` and `Transactions`, and define $N=V+T$.

### Examples
**Example 1**

- Input: ten visits, of which four have no transactions, five have one transaction, and one has three transactions
- Output: `[[0,4],[1,5],[2,0],[3,1]]`
- Explanation: The row for count 2 is required even though no visit belongs to that bucket.

**Example 2**

- Input: two visits and no transactions matching either visit
- Output: `[[0,2]]`

**Example 3**

- Input: one visit with no transactions and one visit with two transactions
- Output: `[[0,1],[1,0],[2,1]]`
