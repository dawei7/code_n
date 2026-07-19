# Split Array with Equal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 548 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-with-equal-sum/) |

## Problem Description
### Goal
Given an integer array `nums`, choose indices $i < j < k$ that act as separators and are themselves excluded from every section. The four sections are `nums[0:i]`, `nums[i+1:j]`, `nums[j+1:k]`, and `nums[k+1:]`, and each must be nonempty.

Return `True` when some valid separator triple makes all four section sums equal, and `False` otherwise. Negative values and zero are included normally in sums, the separator values do not contribute, and equality of only three sections is insufficient. The function returns feasibility rather than the indices or common sum.

### Function Contract
**Inputs**

- `nums`: a list of integers with at least seven elements

**Return value**

- `True` if valid split indices exist; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 2, 1, 2, 1]`
- Output: `True`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5, 6, 7]`
- Output: `False`

**Example 3**

- Input: `nums = [0, 0, 0, 0, 0, 0, 0]`
- Output: `True`
