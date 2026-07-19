# Best Time to Buy and Sell Stock II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 122 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) |

## Problem Description
### Goal
You are given daily prices for one stock in chronological order. You may buy and sell the stock as many times as useful, but you can hold at most one share at a time. Consequently, an existing share must be sold before another purchase can create a new transaction.

Return the maximum total profit across the entire period. Each transaction contributes its later sale price minus its purchase price, and choosing no transaction is valid when no gain is available. The result may combine gains from several separate rising intervals; it is not limited to the profit from one earliest purchase and one latest sale.

### Function Contract
**Inputs**

- `prices`: the stock price for each day in chronological order

**Return value**

The maximum total profit from any valid sequence of non-overlapping transactions.

### Examples
**Example 1**

- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `7`

**Example 2**

- Input: `prices = [1, 2, 3, 4, 5]`
- Output: `4`

**Example 3**

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`
