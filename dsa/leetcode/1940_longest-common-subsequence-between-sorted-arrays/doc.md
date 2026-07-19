# Longest Common Subsequence Between Sorted Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1940 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/) |

## Problem Description
### Goal
You are given a collection `arrays` of integer arrays. Every inner array is
sorted in strictly increasing order. A subsequence may delete any elements
without changing the relative order of those that remain.

Return the longest sequence that is a subsequence of every inner array. Since
all inputs are strictly increasing, every value present in all arrays appears
in the same ascending order, so the required result consists of all such
common values in increasing order.

### Function Contract
**Inputs**

- `arrays`: between 2 and 100 arrays. Each contains between 1 and 100 distinct
  integers in strictly increasing order, and every value is between 1 and 100.

Let $T$ be the total number of entries across all arrays and let $V=100$ be
the fixed value-domain size.

**Return value**

- The longest common subsequence shared by every input array, listed in
  strictly increasing order. Return an empty list when no value is common to
  all arrays.

### Examples
**Example 1**

- Input: `arrays = [[1, 3, 4], [1, 4, 7, 9]]`
- Output: `[1, 4]`

**Example 2**

- Input:
  `arrays = [[2, 3, 6, 8], [1, 2, 3, 5, 6, 7, 10], [2, 3, 4, 6, 9]]`
- Output: `[2, 3, 6]`

**Example 3**

- Input: `arrays = [[1, 2, 3, 4, 5], [6, 7, 8]]`
- Output: `[]`
