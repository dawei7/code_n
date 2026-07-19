# K-diff Pairs in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 532 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/k-diff-pairs-in-an-array/) |

## Problem Description
### Goal
Given an integer array `nums` and a nonnegative integer `k`, a k-diff pair consists of values `(nums[i], nums[j])` whose absolute difference is exactly `k`, using two distinct indices.

Return the number of unique k-diff pairs. Pairs are unique by their values rather than by index choices, and reversing the same two values does not create another result. When $k = 0$, a value qualifies only if it occurs at least twice; when $k > 0$, duplicate occurrences must not multiply an already counted value pair.

### Function Contract
**Inputs**

- `nums`: an integer array that may contain duplicate values
- `k`: a nonnegative target difference

**Return value**

- The number of distinct value pairs `(a, b)` with $a < b$ and $b - a = k$, or repeated-value pairs when $k = 0$

### Examples
**Example 1**

- Input: `nums = [3, 1, 4, 1, 5], k = 2`
- Output: `2`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5], k = 1`
- Output: `4`

**Example 3**

- Input: `nums = [1, 3, 1, 5, 4], k = 0`
- Output: `1`
