# Degree of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 697 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/degree-of-an-array/) |

## Problem Description
### Goal
Given a nonempty array of non-negative integers `nums`, define its degree as the maximum frequency of any one element in the entire array.

Find and return the smallest possible length of a contiguous subarray that has the same degree as `nums`. The subarray may focus on any element tied for the full array's maximum frequency, but it must contain all occurrences needed to reach that frequency within one continuous range; deleting internal positions is not allowed.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- The length of the shortest contiguous subarray with the same degree as `nums`

### Examples
**Example 1**

- Input: `nums = [1,2,2,3,1]`
- Output: `2`

**Example 2**

- Input: `nums = [1,2,2,3,1,4,2]`
- Output: `6`

**Example 3**

- Input: `nums = [1,2,1,3,3]`
- Output: `2`
