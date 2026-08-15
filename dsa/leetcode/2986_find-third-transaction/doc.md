# Find Third Transaction

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2986 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-third-transaction/) |

## Problem Description

### Goal

The `Transactions` table records a user's spend and transaction timestamp. The
pair `(user_id, transaction_date)` is unique, so each user's rows have an
unambiguous chronological order.

For every user with at least three transactions, inspect exactly their third
transaction by date. Return it only when its spend is strictly greater than
the spend of each of the preceding two transactions. Later transactions do not
replace a third transaction that fails the condition. Name the output fields
`user_id`, `third_transaction_spend`, and `third_transaction_date`, and order
the result by `user_id` ascending.

### Function Contract

**Inputs**

- `Transactions(user_id, spend, transaction_date)`: uniquely dated transaction rows per user

Let $R$ be the number of transaction rows.

**Return value**

Return qualifying users' chronological third transactions with the required
aliases, ordered by ascending `user_id`.

### Examples

#### Example 1

- **Input:** User `1` spends `7.44`, `49.78`, then `65.56` chronologically.
- **Output:** `(1, 65.56, "2023-11-18 13:49:42")`

#### Example 2

- **Input:** A user has only two transactions.
- **Output:** No row for that user.

#### Example 3

- **Input:** The third spend is equal to one of the first two spends.
- **Output:** No row, because both comparisons must be strict.
