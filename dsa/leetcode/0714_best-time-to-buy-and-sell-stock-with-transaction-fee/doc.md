# Best Time to Buy and Sell Stock with Transaction Fee

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 714 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) |

## Problem Description
### Goal
Given daily stock prices and a transaction fee, find the maximum profit you can achieve. You may complete as many buy-sell transactions as you like, but you may hold at most one share at a time and therefore must sell before buying again.

The fee is charged exactly once for each completed purchase-and-sale transaction. Return the greatest final profit after any valid sequence of actions, allowing days with no action and allowing no transactions when trading would lose money. A share must be bought before it is sold.

### Function Contract
**Inputs**

- `prices`: the stock price on each consecutive day
- `fee`: the cost charged once for every completed buy-sell transaction

**Return value**

- The greatest achievable final profit

### Examples
**Example 1**

- Input: `prices = [1,3,2,8,4,9], fee = 2`
- Output: `8`

**Example 2**

- Input: `prices = [1,3,7,5,10,3], fee = 3`
- Output: `6`

**Example 3**

- Input: `prices = [1,2,3], fee = 1`
- Output: `1`
