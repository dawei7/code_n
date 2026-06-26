# Combination Sum IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_187` |
| Frontend ID | 377 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [combination-sum-iv](https://leetcode.com/problems/combination-sum-iv/) |

## Problem Description & Examples
### Goal
Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.

Note that different sequences are counted as different combinations.

### Function Contract
**Inputs**

- `nums`: List[int] - distinct integers
- `target`: int

**Return value**

int - number of combinations

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], target = 4`
- Output: `7`

**Example 2**

- Input: `nums = [4], target = 13`
- Output: `0`

**Example 3**

- Input: `nums = [2, 5], target = 2`
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
