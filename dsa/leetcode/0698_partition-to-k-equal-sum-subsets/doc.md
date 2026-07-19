# Partition to K Equal Sum Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 698 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `k`, determine whether the array can be divided into exactly `k` nonempty subsets whose sums are all equal.

Return `True` if such a partition exists and `False` otherwise. Every array occurrence must belong to exactly one subset, even when several occurrences have the same value; subsets need not correspond to contiguous ranges and their internal order is irrelevant. No element may be omitted or reused.

### Function Contract
**Inputs**

- `nums`: a nonempty list of positive integers
- `k`: the required number of subsets, no greater than `len(nums)`

**Return value**

- `true` when such a complete partition exists; otherwise `false`

### Examples
**Example 1**

- Input: `nums = [4,3,2,3,5,2,1], k = 4`
- Output: `true`

**Example 2**

- Input: `nums = [1,2,3,4], k = 3`
- Output: `false`

**Example 3**

- Input: `nums = [3,1], k = 2`
- Output: `false`
