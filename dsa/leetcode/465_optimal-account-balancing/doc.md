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

### Required Complexity

- **Time:** $O(k!)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Discard transaction history after netting balances**

For each payment, subtract the amount from the payer's balance and add it to the recipient's. Only these final net debts and credits matter for settlement; people whose balance is already zero need no further transaction and are removed. The remaining `k` balances sum to zero.

**Settle the first unfinished balance**

Advance past leading zeros. Pair the first nonzero balance with each later balance of the opposite sign. One new transfer can combine them, modeled by adding the first balance into the later one, then recursively settle the remaining suffix. Restore the balance after each branch and take the fewest transfers.

**Why exploring opposite signs is complete**

In some optimal settlement, the first debtor or creditor must transfer with an opposite-signed account. Combining that first transfer leaves the same residual amount represented by the updated partner balance, so every possible optimal first counterparty appears among the recursive branches. Same-signed transfers cannot reduce either side's outstanding obligation and are unnecessary.

**Prune equivalent and exact matches**

At one recursion level, partners with equal balances create identical residual multisets, so try that value once. If a partner exactly cancels the first balance, that one transaction settles both accounts; no alternative partner can settle the first account using fewer than one transaction, so stop considering further branches at that level.

#### Complexity detail

In the worst case, each unfinished balance can branch to many opposite-signed partners, giving $O(k!)$ time for `k` nonzero net balances, though duplicate and exact-match pruning substantially reduce common cases. Recursion and the mutable balance list use $O(k)$ space.

#### Alternatives and edge cases

- **Bitmask subset DP:** partitions balances into zero-sum groups in exponential state space and can offer more predictable bounds, at the cost of larger tables.
- **Unpruned backtracking:** is correct but repeats equal residual states and explores alternatives after exact cancellation.
- **Greedily match largest debt and credit:** can settle balances but does not always minimize the number of transactions.
- **No transactions or all-zero net balances:** requires zero settlement transfers.
- **Repeated equal balances:** symmetry pruning is essential to avoid permuting equivalent partners.
- **Exact opposite pair:** one transfer settles both and justifies an early branch cutoff.
- **Person identifiers:** may be sparse; aggregate them in a map rather than allocating by maximum identifier.

</details>
