# Integer Break

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_189` |
| Frontend ID | 343 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming |
| Official Link | [integer-break](https://leetcode.com/problems/integer-break/) |

## Problem Description & Examples
### Goal
Given an integer `n`, break it into the sum of `k` positive integers, where `k >= 2`, and maximize the product of those integers.

Return the maximum product you can get.

### Function Contract
**Inputs**

- `n`: int

**Return value**

int - maximum product

### Examples
**Example 1**

- Input: `n = 10`
- Output: `36`

**Example 2**

- Input: `n = 3`
- Output: `2`

**Example 3**

- Input: `n = 2`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
