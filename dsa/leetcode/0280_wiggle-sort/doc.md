# Wiggle Sort

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 280 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/wiggle-sort/) |

## Problem Description
### Goal
Given a mutable integer array, rearrange its existing values into wiggle order. Starting at index zero, adjacent comparisons must alternate as `nums[0] <= nums[1] >= nums[2] <= nums[3] >= ...` through the full array.

Modify the array in place and return nothing. Use exactly the original multiset, including every duplicate occurrence, without introducing or deleting values. The inequalities are non-strict, so equal neighbors are allowed and a valid arrangement always exists. Many outputs may satisfy the pattern; any one is acceptable, including the unchanged input when it already has the required alternating comparisons.

### Function Contract
**Inputs**

- `nums`: the mutable integer array

**Return value**

Returns `None`; after in-place mutation, `nums[0] <= nums[1] >= nums[2] <= nums[3] ...`, using exactly the original multiset.

### Examples
**Example 1**

- Input: `nums = [3,5,2,1,6,4]`
- Output: one valid result is `[3,5,1,6,2,4]`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: one valid result is `[1,3,2,4]`

**Example 3**

- Input: `nums = [2,2,2]`
- Output: `[2,2,2]`
