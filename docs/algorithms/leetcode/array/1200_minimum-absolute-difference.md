# Minimum Absolute Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1200 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [minimum-absolute-difference](https://leetcode.com/problems/minimum-absolute-difference/) |

## Problem Description & Examples
### Goal
Find all pairs of values with the smallest absolute difference among any two elements in the array.

### Function Contract
**Inputs**

- `arr`: array of distinct integers.

**Return value**

Pairs `[a, b]` in ascending order where `a < b` and `b - a` is the minimum possible difference.

### Examples
**Example 1**

- Input: `arr = [4,2,1,3]`
- Output: `[[1,2],[2,3],[3,4]]`

**Example 2**

- Input: `arr = [1,3,6,10,15]`
- Output: `[[1,3]]`

**Example 3**

- Input: `arr = [3,8,-10,23,19,-4,-14,27]`
- Output: `[[-14,-10],[19,23],[23,27]]`

---

## Underlying Base Algorithm(s)
Sorting and adjacent comparison.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` for sorting/output depending on implementation.
