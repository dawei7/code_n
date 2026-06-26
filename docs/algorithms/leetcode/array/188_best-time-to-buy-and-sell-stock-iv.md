# Best Time to Buy and Sell Stock IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 188 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [best-time-to-buy-and-sell-stock-iv](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) |

## Problem Description & Examples
### Goal
Given stock prices over time, make at most `k` buy-sell transactions to maximize profit. You must sell before buying again.

### Function Contract
**Inputs**

- `k`: maximum number of transactions.
- `prices`: daily stock prices.

**Return value**

Return the maximum achievable profit.

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

---

## Underlying Base Algorithm(s)
Use DP over transaction count. Maintain `cash[t]`, the best profit after at most `t` completed sells while holding no stock, and `hold[t]`, the best profit while holding a stock after using the `t`th buy. Update these states for each price. If `k >= n / 2`, it reduces to unlimited transactions by summing every positive price difference.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k)`
- **Space Complexity**: `O(k)`
