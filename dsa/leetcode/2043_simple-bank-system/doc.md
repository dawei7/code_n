# Simple Bank System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2043 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/simple-bank-system/) |

## Problem Description

### Goal

A bank has $N$ accounts numbered from `1` through `N`. The 0-indexed array
`balance` supplies their initial balances, so account `i + 1` starts with
`balance[i]`.

Design a `Bank` object that executes deposits, withdrawals, and transfers.
Every referenced account must exist. A withdrawal or transfer is valid only
when its source account contains at least the requested amount. Apply valid
transactions and return `true`; reject invalid transactions without changing
any balance and return `false`.

### Function Contract

Let $N$ be the number of accounts.

**Operations**

- `Bank(balance)` initializes accounts `1` through `N` from the given array.
- `transfer(account1, account2, money)` moves `money` from `account1` to
  `account2` if both accounts exist and the source has sufficient funds.
- `deposit(account, money)` adds `money` when the account exists.
- `withdraw(account, money)` removes `money` when the account exists and has
  sufficient funds.

The constraints are $1 \le N \le 10^5$ and
$0 \le \texttt{balance[i]},\texttt{money}\le10^{12}$. At most $10^4$ calls are
made to each transaction method.

**Return value**

- The constructor returns no value. Every transaction returns whether it was
  valid and applied.

### Examples

**Example 1**

- Input: `operations = ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]`, `arguments = [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]`
- Output: `[null, true, true, true, false, false]`

**Example 2**

- Input: initialize `[5]`, then call `deposit(1, 4)` and `withdraw(1, 10)`
- Output: `[true, false]`
- Explanation: The deposit raises the balance to `9`, which is still
  insufficient for the withdrawal.

**Example 3**

- Input: initialize `[8, 2]`, then call `transfer(1, 2, 3)` and
  `withdraw(2, 4)`
- Output: `[true, true]`
