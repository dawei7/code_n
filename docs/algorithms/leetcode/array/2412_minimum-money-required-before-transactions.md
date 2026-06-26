# Minimum Money Required Before Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2412 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-money-required-before-transactions](https://leetcode.com/problems/minimum-money-required-before-transactions/) |

## Problem Description & Examples
### Goal
Determine the minimum initial capital required to complete a series of transactions. Each transaction consists of a cost (money spent) and a cashback (money returned). If you have enough money to cover the cost, you perform the transaction and your balance decreases by the cost and then increases by the cashback. If you do not have enough, you cannot perform the transaction. The goal is to find the smallest starting amount that allows all transactions to be completed in some optimal order.

### Function Contract
**Inputs**

- `transactions`: A list of lists, where each inner list `[cost, cashback]` represents a transaction.

**Return value**

- An integer representing the minimum initial money required to complete all transactions.

### Examples
**Example 1**

- Input: `transactions = [[2,1],[5,0],[4,2]]`
- Output: `10`

**Example 2**

- Input: `transactions = [[3,0],[3,0],[3,0]]`
- Output: `10`

**Example 3**

- Input: `transactions = [[0,0]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy strategy**. We categorize transactions into two groups: those where `cost > cashback` (net loss) and those where `cost <= cashback` (net gain or break-even). 
1. For net loss transactions, we sort them by `cashback` in descending order to minimize the peak money required.
2. For net gain transactions, we perform them as early as possible to increase our balance.
3. The total initial money is the sum of all net losses plus the maximum "bottleneck" encountered during the sequence.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting of transactions, where `N` is the number of transactions.
- **Space Complexity**: `O(1)` (excluding input storage), as we only use a few variables to track the running balance and the maximum requirement.
