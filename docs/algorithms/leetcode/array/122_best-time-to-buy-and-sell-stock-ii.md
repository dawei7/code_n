# Best Time to Buy and Sell Stock II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_19` |
| Frontend ID | 122 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [best-time-to-buy-and-sell-stock-ii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) |

## Problem Description & Examples
### Goal
Given an integer array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit you can achieve. You may complete as many transactions as you like (buy then sell, buy then sell...), but you must sell the stock before you buy again.

### Function Contract
**Inputs**

- `prices`: List[int]

**Return value**

int - maximum profit

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

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
