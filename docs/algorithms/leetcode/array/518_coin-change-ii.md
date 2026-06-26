# Coin Change II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_197` |
| Frontend ID | 518 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [coin-change-ii](https://leetcode.com/problems/coin-change-ii/) |

## Problem Description & Examples
### Goal
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

### Function Contract
**Inputs**

- `amount`: int
- `coins`: List[int]

**Return value**

int - number of combinations

### Examples
**Example 1**

- Input: `amount = 5, coins = [1, 2, 5]`
- Output: `4`

**Example 2**

- Input: `amount = 17, coins = [1, 3, 7]`
- Output: `12`

**Example 3**

- Input: `amount = 4, coins = [2, 5]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
