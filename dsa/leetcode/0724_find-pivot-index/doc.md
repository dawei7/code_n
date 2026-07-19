# Find Pivot Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 724 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/find-pivot-index/) |

## Problem Description
### Goal
Given an integer array `nums`, a pivot index is an index where the sum of all numbers strictly to its left equals the sum of all numbers strictly to its right. The value at the pivot belongs to neither sum.

Return the leftmost pivot index, or `-1` if none exists. At the left edge, the empty left side has sum `0`; at the right edge, the empty right side also has sum `0`, so either endpoint can qualify under the same rule.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- The smallest pivot index, or `-1` if every index has unequal left and right sums

### Examples
**Example 1**

- Input: `nums = [1,7,3,6,5,6]`
- Output: `3`

**Example 2**

- Input: `nums = [1,2,3]`
- Output: `-1`

**Example 3**

- Input: `nums = [2,1,-1]`
- Output: `0`
