# Find All K-Distant Indices in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2200 |
| Difficulty | Easy |
| Topics | Array, Two Pointers |
| Official Link | [find-all-k-distant-indices-in-an-array](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/) |

## Problem Description & Examples
### Goal
Return every array index lying within distance `k` of at least one occurrence of `key`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `key`: the target value.
- `k`: the maximum allowed absolute index distance.

**Return value**

All qualifying indices in increasing order.

### Examples
**Example 1**

- Input: `nums = [3, 4, 9, 1, 3, 9, 5]`, `key = 9`, `k = 1`
- Output: `[1, 2, 3, 4, 5, 6]`

**Example 2**

- Input: `nums = [2, 2, 2, 2, 2]`, `key = 2`, `k = 2`
- Output: `[0, 1, 2, 3, 4]`

**Example 3**

- Input: `nums = [1, 2, 3]`, `key = 2`, `k = 0`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
Each key occurrence covers the interval `[index - k, index + k]` clipped to array bounds. Scan key positions from left to right and append uncovered indices from these intervals, starting after the last index already emitted. This merges overlaps while preserving sorted order.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the output, with `O(1)` auxiliary state
