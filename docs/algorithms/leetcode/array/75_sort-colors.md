# Sort Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_12` |
| Frontend ID | 75 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Sorting |
| Official Link | [sort-colors](https://leetcode.com/problems/sort-colors/) |

## Problem Description & Examples
### Goal
Given an array containing only `0`, `1`, and `2`, rearrange it in-place so equal values are grouped in increasing order: all `0`s first, then all `1`s, then all `2`s.

### Function Contract
**Inputs**

- `nums`: List[int] containing only 0, 1, and 2

**Return value**

List[int] - the same values in sorted color order

### Examples
**Example 1**

- Input: `nums = [2, 0, 2, 1, 1, 0]`
- Output: `[0, 0, 1, 1, 2, 2]`

**Example 2**

- Input: `nums = [2, 0, 1]`
- Output: `[0, 1, 2]`

**Example 3**

- Input: `nums = [1, 1, 0]`
- Output: `[0, 1, 1]`

---

## Underlying Base Algorithm(s)
Dutch National Flag partitioning with three pointers.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
