# Optimal Account Balancing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 465 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/optimal-account-balancing/) |

## Problem Description
### Goal
Given completed transactions `[from, to, amount]`, compute each person's net balance: payments decrease the payer's balance and increase the receiver's. The original individual transactions need not be reversed directly; only final net debts and credits matter.

Return the minimum number of additional money transfers needed to bring every person's net balance to zero. A settling transfer may be made between any people and for any useful positive amount, and one transfer can eliminate one or both participants' remaining imbalance. People already at zero require no action. The function returns the transaction count rather than a concrete settlement plan.

### Function Contract
**Inputs**

- `transactions`: entries `[from, to, amount]` indicating that `from` paid `amount` to `to`

**Return value**

- The minimum number of additional transfers that can make every net balance zero

### Examples
**Example 1**

- Input: `transactions = [[0, 1, 10], [2, 0, 5]]`
- Output: `2`

**Example 2**

- Input: `transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]`
- Output: `1`

**Example 3**

- Input: `transactions = []`
- Output: `0`
