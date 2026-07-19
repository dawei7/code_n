# Best Time to Buy and Sell Stock III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 123 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) |

## Problem Description
### Goal
You are given the price of a stock for each day in chronological order. Choose a trading schedule containing at most two completed transactions, where each transaction buys one share and sells it on a later day. You cannot hold more than one share, so a second purchase can occur only after the first holding has been sold.

Return the maximum combined profit attainable with zero, one, or two transactions. The two transactions may use different profitable intervals and do not both have to be present. If every possible sale loses money, return `0`; never count an unfinished purchase or allow the same held share to be sold twice.

### Function Contract
**Inputs**

- `prices`: stock prices in chronological order

**Return value**

The maximum profit attainable with zero, one, or two completed transactions.

### Examples
**Example 1**

- Input: `prices = [3, 3, 5, 0, 0, 3, 1, 4]`
- Output: `6`

**Example 2**

- Input: `prices = [1, 2, 3, 4, 5]`
- Output: `4`

**Example 3**

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`
