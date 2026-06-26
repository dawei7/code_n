# Merge Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_222` |
| Frontend ID | 56 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [merge-intervals](https://leetcode.com/problems/merge-intervals/) |

## Problem Description & Examples
### Goal
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Function Contract
**Inputs**

- `intervals`: List[List[int]]

**Return value**

List[List[int]] - merged intervals

### Examples
**Example 1**

- Input: `intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]`
- Output: `[[1, 6], [8, 10], [15, 18]]`

**Example 2**

- Input: `intervals = [[14, 15], [9, 14]]`
- Output: `[[9, 15]]`

**Example 3**

- Input: `intervals = [[19, 20]]`
- Output: `[[19, 20]]`

---

## Underlying Base Algorithm(s)
- [Activity selection / interval choice](greedy_01_activity-selection.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
