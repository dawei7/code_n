# Arithmetic Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1630 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting |
| Official Link | [arithmetic-subarrays](https://leetcode.com/problems/arithmetic-subarrays/) |

## Problem Description & Examples
### Goal
For each query range, decide whether the selected subarray can be rearranged
into an arithmetic progression.

### Function Contract
**Inputs**

- `nums`: the base integer array.
- `l`: left endpoints of the queries.
- `r`: right endpoints of the queries.

**Return value**

A boolean result for each query.

### Examples
**Example 1**

- Input: `nums = [4, 6, 5, 9, 3, 7], l = [0, 0, 2], r = [2, 3, 5]`
- Output: `[true, false, true]`

**Example 2**

- Input: `nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], l = [0, 1, 6, 4, 8, 7], r = [4, 4, 9, 7, 9, 10]`
- Output: `[false, true, false, false, true, true]`

**Example 3**

- Input: `nums = [1, 3, 5], l = [0], r = [2]`
- Output: `[true]`

---

## Underlying Base Algorithm(s)
For each query, copy the requested slice, sort it, and verify that every adjacent
difference equals the first adjacent difference. Each query is independent.

---

## Complexity Analysis
- **Time Complexity**: `O(q * k log k)` for query length `k` in the direct method.
- **Space Complexity**: `O(k)` per query slice.
