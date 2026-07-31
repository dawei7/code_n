# Minimum Money Required Before Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2412 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-money-required-before-transactions/) |

## Problem Description

### Goal

Each entry `transactions[i] = [cost_i, cashback_i]` describes one transaction that must be performed exactly once. Immediately before transaction $i$, the current money must be at least `cost_i`. Completing it changes the balance to `money - cost_i + cashback_i`, so the transaction may either lose money, break even, or increase the balance.

Choose the smallest amount of money that is sufficient before any transaction even when the transactions are presented in any possible order. The guarantee must therefore cover the most demanding ordering, rather than an order selected to build capital early. Return that minimum universally sufficient initial balance.

### Function Contract

**Inputs**

- `transactions`: A non-empty array whose entries are `[cost, cashback]` pairs.

Let $n = \lvert\texttt{transactions}\rvert$. The contract guarantees $1 \le n \le 10^5$ and $0 \le \texttt{cost}, \texttt{cashback} \le 10^9$.

**Return value**

Return the minimum initial money that allows every transaction to complete regardless of their order.

### Examples

**Example 1**

- Input: `transactions = [[2,1],[5,0],[4,2]]`
- Output: `10`

**Example 2**

- Input: `transactions = [[3,0],[0,3]]`
- Output: `3`

**Example 3**

- Input: `transactions = [[0,0]]`
- Output: `0`
