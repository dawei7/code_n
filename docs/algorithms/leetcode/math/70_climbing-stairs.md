# Climbing Stairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_174` |
| Frontend ID | 70 |
| Difficulty | Easy |
| Topics | Math, Dynamic Programming, Memoization |
| Official Link | [climbing-stairs](https://leetcode.com/problems/climbing-stairs/) |

## Problem Description & Examples
### Goal
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

### Function Contract
**Inputs**

- `n`: int

**Return value**

int - number of distinct ways

### Examples
**Example 1**

- Input: `n = 3`
- Output: `3`

**Example 2**

- Input: `n = 2`
- Output: `2`

**Example 3**

- Input: `n = 1`
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
