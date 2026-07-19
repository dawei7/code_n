# Best Time to Buy and Sell Stock IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 188 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) |

## Problem Description
### Goal
You are given daily prices for one stock and a nonnegative limit `k`. Complete at most `k` transactions, where each transaction buys one share on one day and sells that share on a later day. You may not hold more than one share, so transactions cannot overlap.

Return the greatest total profit obtainable across the full price history. Using fewer than `k` transactions, including none, is allowed when additional trades offer no gain. A later transaction may begin only after the preceding share has been sold, and unfinished purchases contribute nothing. The output is the maximum profit amount rather than the chosen trading days.

### Function Contract
**Inputs**

- `k`: maximum completed transactions
- `prices`: daily stock prices

**Return value**

The greatest achievable profit.

### Examples
**Example 1**

- Input: `k = 2, prices = [2,4,1]`
- Output: `2`

**Example 2**

- Input: `k = 2, prices = [3,2,6,5,0,3]`
- Output: `7`

**Example 3**

- Input: `k = 0, prices = [1,3,5]`
- Output: `0`
