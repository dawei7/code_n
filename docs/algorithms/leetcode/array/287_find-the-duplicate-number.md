# Find the Duplicate Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_81` |
| Frontend ID | 287 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Bit Manipulation |
| Official Link | [find-the-duplicate-number](https://leetcode.com/problems/find-the-duplicate-number/) |

## Problem Description & Examples
### Goal
Given a linked list (as array) and a value `x`, partition it such that all nodes with values less than `x` come before nodes with values >= `x`. Preserve relative order.

### Function Contract
**Inputs**

- `head`: List[int]
- `x`: int - partition value

**Return value**

List[int] - partitioned list

### Examples
**Example 1**

- Input: `head = [1, 4, 3, 2, 5, 2], x = 3`
- Output: `[1, 2, 2, 4, 3, 5]`

**Example 2**

- Input: `head = [7, 7], x = 2`
- Output: `[7, 7]`

**Example 3**

- Input: `head = [3, 10], x = 3`
- Output: `[3, 10]`

---

## Underlying Base Algorithm(s)
trivial

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
