# Count Salary Categories

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1907 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Count Salary Categories](https://leetcode.com/problems/count-salary-categories/) |

## Problem Description

### Goal

The `Accounts` table contains one row per bank account and records that account's monthly `income`. Classify every account into exactly one salary category: `"Low Salary"` for income strictly below `20000`, `"Average Salary"` for income from `20000` through `50000` inclusive, and `"High Salary"` for income strictly above `50000`.

Return one row for each of these three category names with the number of matching accounts. All three rows are mandatory even when a category has no accounts, in which case its count must be zero. Result row order is unrestricted.

### Function Contract

**Input table**

- `Accounts(account_id, income)`
- `account_id` is the table's unique primary key.
- `income` is the account's monthly income.

**Return value**

Return columns `category` and `accounts_count`, with exactly one row for each required salary category and its count.

### Examples

**Example 1**

- Input rows: `(3, 108939)`, `(2, 12747)`, `(8, 87709)`, `(6, 91796)`
- Output rows: `("Low Salary", 1)`, `("Average Salary", 0)`, `("High Salary", 3)`

**Example 2**

- Input rows: `(1, 20000)`, `(2, 50000)`
- Output rows: `("Low Salary", 0)`, `("Average Salary", 2)`, `("High Salary", 0)`

**Example 3**

- Input: an empty `Accounts` table
- Output: all three categories with count `0`

### Required Complexity

- **Time:** $O(A)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Make the output categories structural.** Use three `SELECT` branches joined with `UNION ALL`, one branch per required label. Each branch always emits one aggregate row, even when `Accounts` is empty or no row satisfies its condition. This guarantees the complete three-row output without depending on which categories occur in the data.

**Count conditionally.** In each branch, place `1` inside a `CASE` only when the income belongs to that branch's interval and leave other rows as `NULL`. `COUNT(expression)` ignores `NULL`, so it returns exactly the number of matching accounts and naturally yields zero when there are none. The interval predicates are disjoint and cover every income.

`UNION ALL` preserves the three independently labeled rows without unnecessary duplicate elimination; their category literals are already distinct.

#### Complexity detail

Let $A$ be the number of `Accounts` rows. Each of the three fixed aggregate branches scans the table once, so total time is $O(3A)=O(A)$. Each branch maintains one counter and the output has exactly three rows, giving $O(1)$ auxiliary result state.

#### Alternatives and edge cases

- **Group a computed category:** A `CASE` plus `GROUP BY` scans once, but categories absent from the input disappear unless joined to a separate category relation.
- **Use `SUM(condition)`:** This is concise in MySQL, but `SUM` over an empty table is `NULL` unless wrapped with `COALESCE`; conditional `COUNT` returns zero directly.
- **Boundary `20000`:** It belongs to `"Average Salary"`, not `"Low Salary"`.
- **Boundary `50000`:** It also belongs to `"Average Salary"`, while high salary starts strictly above it.
- **Empty table:** Aggregate branches must still emit all three zero rows.
- **Output order:** The contract accepts any row order, so no `ORDER BY` is required.

</details>
