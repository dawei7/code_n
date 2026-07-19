# Wiggle Sort II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 324 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Greedy, Sorting, Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/wiggle-sort-ii/) |

## Problem Description
### Goal
Given a mutable integer array, rearrange its existing occurrences into strict wiggle order: `nums[0] < nums[1] > nums[2] < nums[3] > ...`. Every odd position must be strictly greater than both adjacent even positions that exist.

Modify the input in place and return nothing, preserving the complete original multiset including duplicates. A valid arrangement is guaranteed, although careless placement of equal values can violate a strict inequality. Any valid permutation is accepted. Meet the intended linear-time and constant-extra-space target rather than returning a separately sorted array.

### Function Contract
**Inputs**

- `nums`: the mutable integer array to rearrange

**Return value**

No separate value. The input array itself must become a strict wiggle permutation of its original multiset.

### Examples
**Example 1**

- Input: `nums = [1,5,1,1,6,4]`
- Valid result: `[1,6,1,5,1,4]`

**Example 2**

- Input: `nums = [1,3,2,2,3,1]`
- Valid result: `[2,3,1,3,1,2]`

**Example 3**

- Input: `nums = [1,1,2,2,2,1]`
- Valid result: `[1,2,1,2,1,2]`
