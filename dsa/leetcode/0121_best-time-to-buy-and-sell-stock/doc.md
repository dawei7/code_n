# Best Time to Buy and Sell Stock

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 121 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |

## Problem Description
### Goal
You are given the price of one stock on each day in chronological order. You may complete at most one transaction by choosing one day to buy a share and a strictly later day to sell that same share. Selling before buying, short-selling, and holding multiple shares are not allowed.

Return the greatest profit obtainable from a valid buy-sell pair. You may choose not to trade, so the result is `0` when prices never rise after a purchase opportunity. Profit is the sale price minus the earlier purchase price; the task is not to report the days or the two prices themselves.

### Function Contract
**Inputs**

- `prices`: the stock price for each day in chronological order

**Return value**

The maximum profit from at most one buy followed by one sale.

### Examples
**Example 1**

- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `5`

**Example 2**

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`

**Example 3**

- Input: `prices = [2, 4, 1]`
- Output: `2`
