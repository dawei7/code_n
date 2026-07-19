# Find All Numbers Disappeared in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 448 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) |

## Problem Description
### Goal
Given an integer array `nums` of length `n`, every entry lies in the inclusive range `1..n`, but some values may occur more than once. Determine which values from that complete range have no occurrence in the array.

Return all missing values. Duplicate input occurrences do not create extra output and may correspond to several absent values elsewhere. Meet the required linear time and constant auxiliary space beyond the returned list; modifying the input array to mark observed values is permitted. An array containing every range value once returns an empty list.

### Function Contract
**Inputs**

- `nums`: an integer array of length `n` whose values all lie in `[1, n]`

**Return value**

- Return all missing values from `[1, n]`, in increasing order. The input array may be modified.

### Examples
**Example 1**

- Input: `nums = [4, 3, 2, 7, 8, 2, 3, 1]`
- Output: `[5, 6]`

**Example 2**

- Input: `nums = [1, 1]`
- Output: `[2]`

**Example 3**

- Input: `nums = [1]`
- Output: `[]`
