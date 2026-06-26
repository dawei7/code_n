# Best Time to Buy and Sell Stock III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 123 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [best-time-to-buy-and-sell-stock-iii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) |

## Problem Description & Examples
### Goal
Given daily stock prices, maximize profit using at most two buy-sell transactions. A new transaction can start only after the previous one has sold.

### Function Contract
**Inputs**

- `prices`: stock price by day.

**Return value**

The maximum profit possible with at most two transactions.

### Examples
**Example 1**

- Input: `prices = [3,3,5,0,0,3,1,4]`
- Output: `6`

**Example 2**

- Input: `prices = [1,2,3,4,5]`
- Output: `4`

**Example 3**

- Input: `prices = [7,6,4,3,1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Constant-state dynamic programming for stock trading.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
