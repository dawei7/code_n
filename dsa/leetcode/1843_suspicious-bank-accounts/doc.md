# Suspicious Bank Accounts

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/suspicious-bank-accounts/) |
| Frontend ID | 1843 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

`Accounts` assigns each bank account a maximum expected monthly income. `Transactions` records deposits and withdrawals: a `Creditor` row adds money to an account, whereas a `Debtor` row removes money and does not count as income.

For every account and calendar month, total only its creditor amounts. An account is suspicious when that monthly income is strictly greater than its own `max_income` during at least two consecutive calendar months. Report the identifiers of all accounts satisfying that condition.

### Function Contract

**Inputs**

- `Accounts(account_id, max_income)`:
  - `account_id` is unique.
  - `max_income` is that account's permitted monthly income threshold.
- `Transactions(transaction_id, account_id, type, amount, day)`:
  - `transaction_id` is unique.
  - `type` is either `'Creditor'` for a deposit or `'Debtor'` for a withdrawal.
  - `amount` is the transaction amount.
  - `day` is the transaction timestamp.
- Let $r$ be the number of transaction rows.

**Return value**

- Return one column named `account_id`.
- Include an account once if its total creditor income exceeds `max_income` in two calendar months whose distance is exactly one month.
- Return the rows in any order.

### Examples

**Example 1**

For account 3, the creditor transactions total 300100 in June 2021 and 64900 in July 2021. Both totals exceed its threshold of 21000, so account 3 is suspicious.

Account 4 exceeds its threshold in May and July, but its June income does not exceed the threshold. The qualifying months are not consecutive, so account 4 is excluded.

Output:

| account_id |
|---:|
| 3 |

**Example 2**

If an account's income equals its threshold in January and exceeds it in February, the account is not suspicious because the January comparison must be strict.

**Example 3**

December 2023 and January 2024 are consecutive calendar months. An account exceeding its threshold in both must be reported despite the year boundary.
