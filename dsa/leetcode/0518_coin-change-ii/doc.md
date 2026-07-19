# Coin Change II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 518 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/coin-change-ii/) |

## Problem Description
### Goal
Given an integer `amount` and an array of unique positive coin denominations, choose any nonnegative number of coins of each denomination. The supply of every coin kind is infinite, and selected values must sum exactly to `amount`.

Return the number of combinations that make the amount. Coin order does not distinguish combinations, so `[1, 2]` and `[2, 1]` describe the same choice of counts. Return `0` when a positive amount cannot be formed; for amount zero, choosing no coins is one valid combination. The result is a count, not a minimum coin total.

### Function Contract
**Inputs**

- `amount`: a nonnegative target total
- `coins`: an array of distinct positive denominations, each available without limit

**Return value**

- The number of denomination-count combinations totaling `amount`, or `0` if none exists

### Examples
**Example 1**

- Input: `amount = 5, coins = [1, 2, 5]`
- Output: `4`

**Example 2**

- Input: `amount = 3, coins = [2]`
- Output: `0`

**Example 3**

- Input: `amount = 10, coins = [10]`
- Output: `1`
