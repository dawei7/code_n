# Longest Arithmetic Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1027 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming |
| Official Link | [longest-arithmetic-subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence/) |

## Problem Description & Examples
### Goal
Given an integer array, return the length of the longest subsequence whose adjacent differences are all the same.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - maximum arithmetic subsequence length

### Examples
**Example 1**

- Input: `nums = [3, 6, 9, 12]`
- Output: `4`

**Example 2**

- Input: `nums = [9, 4, 7, 2, 10]`
- Output: `3`

**Example 3**

- Input: `nums = [20, 1, 15, 3, 10, 5, 8]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Dynamic programming by ending index and difference.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`
