# 3Sum Smaller

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 259 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/3sum-smaller/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `target`, consider every triple of distinct positions with indices $i < j < k$. A triple qualifies when `nums[i] + nums[j] + nums[k]` is strictly smaller than `target`.

Return the number of qualifying index triples. Duplicate values at different positions create separate triples, while permutations of the same three positions do not. Sums equal to the target are excluded. Arrays with fewer than three elements return `0`. The function reports only the count, not the value combinations or indices, and must account for all later choices efficiently after ordering the data.

### Function Contract
**Inputs**

- `nums`: an integer array
- `target`: the exclusive upper bound for a triple sum

**Return value**

The number of triples $i < j < k$ satisfying `nums[i] + nums[j] + nums[k] < target`.

### Examples
**Example 1**

- Input: `nums = [-2,0,1,3], target = 2`
- Output: `2`

**Example 2**

- Input: `nums = [], target = 0`
- Output: `0`

**Example 3**

- Input: `nums = [0,0,0], target = 1`
- Output: `1`
