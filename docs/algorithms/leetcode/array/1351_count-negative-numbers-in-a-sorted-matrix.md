# Count Negative Numbers in a Sorted Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1351 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Matrix |
| Official Link | [count-negative-numbers-in-a-sorted-matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) |

## Problem Description & Examples
### Goal
Count negative values in a matrix where every row and every column is sorted in non-increasing order.

### Function Contract
**Inputs**

- `grid`: sorted integer matrix.

**Return value**

The number of negative entries.

### Examples
**Example 1**

- Input: `grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`
- Output: `8`

**Example 2**

- Input: `grid = [[3,2],[1,0]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,-1],[-1,-1]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Staircase scan on a sorted matrix.

---

## Complexity Analysis
- **Time Complexity**: `O(m + n)`
- **Space Complexity**: `O(1)`
