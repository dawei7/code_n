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
