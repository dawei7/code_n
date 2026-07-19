# Increasing Triplet Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 334 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/increasing-triplet-subsequence/) |

## Problem Description
### Goal
Given an integer array, determine whether it contains three positions $i < j < k$ whose values satisfy `nums[i] < nums[j] < nums[k]`. The selected elements form a subsequence and therefore do not need to be contiguous.

Return `True` when any strictly increasing triplet exists and `False` otherwise. Equal values cannot satisfy either strict comparison, and the original index order cannot be rearranged even if the values would sort into a triplet. Meet the required linear running time and constant extra space; the function need not return the indices or values of a qualifying triplet.

### Function Contract
**Inputs**

- `nums`: the integer array

**Return value**

`True` if an increasing subsequence of length three exists; otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5]`
- Output: `True`

**Example 2**

- Input: `nums = [5,4,3,2,1]`
- Output: `False`

**Example 3**

- Input: `nums = [2,1,5,0,4,6]`
- Output: `True`
