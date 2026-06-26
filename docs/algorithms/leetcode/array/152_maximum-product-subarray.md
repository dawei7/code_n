# Maximum Product Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_183` |
| Frontend ID | 152 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [maximum-product-subarray](https://leetcode.com/problems/maximum-product-subarray/) |

## Problem Description & Examples
### Goal
Given an integer array `nums`, find a subarray that has the largest product, and return the product.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - maximum product of a subarray

### Examples
**Example 1**

- Input: `nums = [2, 3, -2, 4]`
- Output: `6`

**Example 2**

- Input: `nums = [1]`
- Output: `1`

**Example 3**

- Input: `nums = [-3, 4]`
- Output: `4`

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
