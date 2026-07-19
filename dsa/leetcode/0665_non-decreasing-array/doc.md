# Non-decreasing Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 665 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/non-decreasing-array/) |

## Problem Description
### Goal
Given an integer array `nums`, determine whether it can become non-decreasing by modifying the value of at most one element. An array is non-decreasing when `nums[i] <= nums[i + 1]` for every valid adjacent pair of indices.

Return `True` if zero or one value changes can make the whole array satisfy that condition, and `False` otherwise. You may replace the chosen value by any integer, but you may not reorder, insert, or delete elements; fixing one inversion must not create another violation with the changed element's other neighbor.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers

**Return value**

- `True` if zero or one value change can make every adjacent pair nondecreasing; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [4, 2, 3]`
- Output: `True`

**Example 2**

- Input: `nums = [4, 2, 1]`
- Output: `False`

**Example 3**

- Input: `nums = [3, 4, 2, 3]`
- Output: `False`
