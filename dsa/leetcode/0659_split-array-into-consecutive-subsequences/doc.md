# Split Array into Consecutive Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 659 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) |

## Problem Description
### Goal
You are given an integer array `nums` sorted in non-decreasing order. Determine whether all of its occurrences can be split into one or more subsequences such that every subsequence is a consecutive increasing sequence, with each integer exactly one greater than the previous integer.

Every resulting subsequence must have length `3` or more. Return `True` if such a complete split is possible and `False` otherwise. Each input occurrence must belong to exactly one subsequence; duplicate values are separate occurrences, and relative order is preserved within each subsequence.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers sorted in non-decreasing order; duplicate values represent distinct occurrences

**Return value**

- `True` if all occurrences can be partitioned into valid consecutive subsequences; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 3, 4, 5]`
- Output: `True`

**Example 2**

- Input: `nums = [1, 2, 3, 3, 4, 4, 5, 5]`
- Output: `True`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 4, 5]`
- Output: `False`
