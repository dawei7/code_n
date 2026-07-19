# Third Maximum Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 414 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/third-maximum-number/) |

## Problem Description
### Goal
Given a nonempty integer array, rank its distinct values from largest to smallest. Duplicate occurrences occupy only one distinct rank, regardless of how often they appear in the input.

Return the value at the third distinct rank when at least three different values exist. If there are fewer than three distinct values, return the overall maximum instead. Negative values, zero, and the smallest representable integer must be treated as ordinary candidates rather than sentinel states. The task returns a value, not its source index or frequency.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- Return the third distinct maximum when it exists; otherwise return the overall maximum.

### Examples
**Example 1**

- Input: `nums = [3,2,1]`
- Output: `1`

**Example 2**

- Input: `nums = [1,2]`
- Output: `2`

**Example 3**

- Input: `nums = [2,2,3,1]`
- Output: `1`
