# Array Nesting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 565 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/array-nesting/) |

## Problem Description
### Goal
Given an integer array `nums` of length `n` whose values are unique and lie in the inclusive range $[0, n - 1]$, form a nesting set from any starting index `k`. Begin with `nums[k]`, then repeatedly use the current value as the next index: `nums[nums[k]]`, `nums[nums[nums[k]]]`, and so on.

Stop before adding a value that already belongs to the set. Return the maximum number of distinct values in a nesting set over all possible starting indices. Because the values form a permutation of valid indices, every sequence eventually enters a cycle rather than leaving the array.

### Function Contract
**Inputs**

- `nums`: a permutation of the integers from `0` through $n - 1$

**Return value**

- The size of the largest nesting set

### Examples
**Example 1**

- Input: `nums = [5, 4, 0, 3, 1, 6, 2]`
- Output: `4`

**Example 2**

- Input: `nums = [0, 1, 2]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 0]`
- Output: `2`
