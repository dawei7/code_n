# Bank Account Summary II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1587 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/bank-account-summary-ii/) |

## Problem Description
### Goal

The `Users` table associates each bank account with its uniquely named owner. The `Transactions` table records changes to account balances: a positive `amount` adds money and a negative `amount` removes money. Every account begins with a zero balance.

Compute each account's balance as the sum of all its transaction amounts. Report the owner's name and resulting balance only when that balance is strictly greater than `10000`. A balance equal to the threshold does not qualify.

Return the qualifying rows in any order.

### Function Contract
**Inputs**

- `Users(account, name)`: one row per account; `account` is unique, and user names are also distinct.
- `Transactions(trans_id, account, amount, transacted_on)`: transaction rows keyed by `trans_id`; `account` identifies the affected user, and signed `amount` records the balance change.

Let $U$ be the number of users and $T$ the number of transactions.

**Return value**

Return columns `name` and `balance`, with one row for every user whose summed transaction amount is greater than `10000`.

### Examples
**Example 1**

- Input: Alice has amounts `7000`, `7000`, and `-3000`; Bob has `1000`; Charlie has `6000`, `6000`, and `-4000`
- Output: `[Alice, 11000]`

**Example 2**

- Input: one account has a single transaction of `10000`
- Output: an empty result because the comparison is strict

**Example 3**

- Input: Ann has `15000` and `-4000`, while Ben has `9000` and `2000`
- Output: `[Ann, 11000]` and `[Ben, 11000]`
