# Minimum Absolute Difference Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1906 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [minimum-absolute-difference-queries](https://leetcode.com/problems/minimum-absolute-difference-queries/) |

## Problem Description & Examples
### Goal
For each query range, find the minimum absolute difference between any two distinct values appearing in that subarray. Values are small positive integers.

### Function Contract
**Inputs**

- `nums`: a list of integers in a small bounded range.
- `queries`: a list of `[left, right]` ranges.

**Return value**

Return the minimum difference for every query, or `-1` if the range contains fewer than two distinct values.

### Examples
**Example 1**

- Input: `nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]`
- Output: `[2,1,4,1]`

**Example 2**

- Input: `nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]`
- Output: `[-1,1,1,3]`

**Example 3**

- Input: `nums = [1,1,1], queries = [[0,2]]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Build prefix frequency counts for each possible value. For a query, determine which values appear by subtracting prefix counts at the range boundaries. Scan the present values in increasing order and compute the smallest gap between consecutive present values.

---

## Complexity Analysis
- **Time Complexity**: `O((n + q) * V)`, where `V` is the value range size
- **Space Complexity**: `O(n * V)`
