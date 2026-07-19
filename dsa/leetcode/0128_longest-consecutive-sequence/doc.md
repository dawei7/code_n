# Longest Consecutive Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 128 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) |

## Problem Description
### Goal
Given an unsorted list of integers, find the longest run of values that could be arranged as consecutive numbers. Values belong to the same run when each successive value is exactly one greater than the previous one; their original positions and order in the list do not matter.

Return the number of distinct integer values in the longest run. Duplicate occurrences do not extend a sequence, gaps divide separate runs, and negative values can participate normally across zero. An empty input has answer `0`, while any nonempty input has at least a one-value sequence even when no two values are consecutive. The required algorithm runs in $O(n)$ time.

### Function Contract
**Inputs**

- `nums`: an unsorted list of integers, possibly containing duplicates

**Return value**

The maximum number of distinct consecutive integer values present, or `0` for an empty list.

### Examples
**Example 1**

- Input: `nums = [100, 4, 200, 1, 3, 2]`
- Output: `4`

**Example 2**

- Input: `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`
- Output: `9`

**Example 3**

- Input: `nums = []`
- Output: `0`
