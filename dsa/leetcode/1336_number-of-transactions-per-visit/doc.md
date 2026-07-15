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

### Required Complexity
- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Count transactions without losing empty visits**

Left join `Visits` to `Transactions` on both `user_id` and the matching date. Group by the visit's composite key and use `COUNT(transaction_date)`. Counting a nullable column, rather than `COUNT(*)`, gives zero for a visit whose left join produced only the placeholder row.

**Generate the complete bucket range**

Find the largest per-visit count. A recursive common table expression starts at 0 and emits the next integer until it reaches that maximum. Left join this generated series to the per-visit counts, group by the generated integer, and count matching visits. Because the series is the preserved side, transaction counts that never occur still produce a row with zero.

Finally, order by the generated count. Every visit contributes to exactly one bucket because its transaction count was computed once from its matching rows, and the complete integer series proves that no required gap can disappear.

#### Complexity detail

With indexed or sort-based grouping, joining and aggregating $N$ input rows takes $O(N\log N)$ time in the general comparison model. Generating and aggregating at most $T+1$ buckets stays within that bound. The grouped visits, bucket series, and database working structures use $O(N)$ space.

#### Alternatives and edge cases

- **Correlated count per visit:** Counting matching `Transactions` in a scalar subquery is concise but may rescan all $T$ transactions for each visit, taking $O(VT)$ time.
- **Group transactions before joining:** Pre-aggregating by user and date is also efficient, provided the subsequent left join preserves visits with no match.
- **No transactions:** The maximum visit count is zero, so the output still contains the single bucket `[0, V]`.
- **Missing intermediate count:** Generate it explicitly and report zero visits.
- **Composite match:** Equal dates from different users, or different dates for one user, must not be combined.
- **Duplicate transaction rows:** Each row represents a separate transaction and contributes to the visit's count.
- **Unmatched transaction:** A transaction with no corresponding visit does not create a visit or a bucket contribution.

</details>
