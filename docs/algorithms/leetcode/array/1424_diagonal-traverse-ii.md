# Diagonal Traverse II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1424 |
| Difficulty | Medium |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Official Link | [diagonal-traverse-ii](https://leetcode.com/problems/diagonal-traverse-ii/) |

## Problem Description & Examples
### Goal
Traverse a jagged list of rows by diagonals. Elements with the same `row + column` belong to the same diagonal, and each diagonal is output from lower row to higher row.

### Function Contract
**Inputs**

- `nums`: a list of integer rows, where rows may have different lengths.

**Return value**

A flat list containing the diagonal traversal order.

### Examples
**Example 1**

- Input: `nums = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[1,4,2,7,5,3,8,6,9]`

**Example 2**

- Input: `nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]`
- Output: `[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]`

**Example 3**

- Input: `nums = [[1],[2,3],[4,5,6]]`
- Output: `[1,2,4,3,5,6]`

---

## Underlying Base Algorithm(s)
Diagonal bucketing. Group values by `row + column`, append while scanning top to bottom, then read each bucket in reverse insertion order.

---

## Complexity Analysis
- **Time Complexity**: `O(N)` where `N` is the total number of values.
- **Space Complexity**: `O(N)`
