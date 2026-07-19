# Account Balance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2066 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/account-balance/) |

## Problem Description

### Goal

The `Transactions` table records deposits and withdrawals for bank accounts. Each account has at most one transaction on a given day. A `Deposit` increases its account's balance by `amount`, while a `Withdraw` decreases the balance by that amount.

Every account begins with balance zero, and the data guarantees that no account's balance becomes negative. Report the balance of each account immediately after every transaction. Sort the result by `account_id` in ascending order and then by `day` in ascending order.

### Function Contract

**Inputs**

- `Transactions(account_id, day, type, amount)`: one row per transaction; `(account_id, day)` is unique, `type` is either `Deposit` or `Withdraw`, and `amount` is a positive integer.

Let $R$ be the number of rows in `Transactions`.

**Return value**

- Return the columns `account_id`, `day`, and `balance`, with one output row per transaction.
- Order rows by `account_id` ascending, then `day` ascending.

### Examples

**Example 1**

- Input: account `1` deposits `2000`, withdraws `1000`, then deposits `3000`; account `2` deposits and later withdraws `7000`.
- Output: balances `2000`, `1000`, and `4000` for account `1`, followed by `7000` and `0` for account `2`.
- Explanation: Each balance is the signed running total within its account through that transaction's day.

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Convert transaction types into signed changes**

Use a `CASE` expression to keep a deposit's `amount` positive and negate a withdrawal's amount. This turns the account balance into a running sum of signed transaction changes.

**Use an account-partitioned running window**

Apply `SUM(...) OVER (...)`, partitioning rows by `account_id` and ordering each partition by `day`. Because `(account_id, day)` is unique, each window position corresponds to exactly one transaction and its cumulative sum is the balance immediately afterward. Finally, order the produced rows by account and day; the window's logical ordering defines the calculation, while the query-level `ORDER BY` guarantees the required presentation order.

Within each account, the signed changes through a row's date are precisely all deposits minus all withdrawals made up to that moment. Their cumulative sum therefore equals the promised account balance. Partitioning prevents transactions from another account from entering that sum, so every output row receives exactly its own account's correct running balance.

#### Complexity detail

Ordering the $R$ rows for window evaluation and final output costs $O(R\log R)$ time in the general case. The database may retain sorted rows and window state proportional to the input, giving $O(R)$ auxiliary space. A matching index can reduce physical sorting work, but the stated bound does not assume one.

#### Alternatives and edge cases

- **Correlated prefix subquery:** Summing all earlier transactions separately for every row is correct, but it can rescan the table and require $O(R^2)$ time.
- **Self-join and aggregation:** Joining each transaction to all earlier rows of the same account also computes the balance, but materializes the same quadratic relationship.
- The first transaction of an account starts from zero rather than inheriting another account's balance.
- A withdrawal contributes a negative change even though `amount` itself is stored as a positive number.
- A balance may become exactly zero; the contract only rules out negative balances.
- Input row order is irrelevant because both the window and result explicitly order by `day`.

</details>
