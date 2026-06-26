# Non-overlapping Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_223` |
| Frontend ID | 435 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Official Link | [non-overlapping-intervals](https://leetcode.com/problems/non-overlapping-intervals/) |

## Problem Description & Examples
### Goal
Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

### Function Contract
**Inputs**

- `intervals`: List[List[int]]

**Return value**

int - minimum intervals to remove

### Examples
**Example 1**

- Input: `intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]`
- Output: `1`

**Example 2**

- Input: `intervals = [[14, 15], [9, 14]]`
- Output: `0`

**Example 3**

- Input: `intervals = [[19, 20]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
- [Activity selection / interval choice](greedy_01_activity-selection.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
