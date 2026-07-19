# 132 Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 456 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Stack, Monotonic Stack, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/132-pattern/) |

## Problem Description
### Goal
Given an integer array, look for a subsequence of three positions $i < j < k$ whose values form a `132` pattern: `nums[i] < nums[k] < nums[j]`. The names describe relative sizes, with the first selected value smallest, the second largest, and the third strictly between them.

Return `True` when any qualifying triple exists and `False` otherwise. Selected positions need not be contiguous, but their index order cannot change. Equal values cannot satisfy either strict inequality. Arrays with fewer than three elements return `False`, and the function need not return the indices or values of a found pattern.

### Function Contract
**Inputs**

- `nums`: an integer array

**Return value**

- `True` if a strict 132 pattern exists; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `False`

**Example 2**

- Input: `nums = [3, 1, 4, 2]`
- Output: `True`

**Example 3**

- Input: `nums = [-1, 3, 2, 0]`
- Output: `True`
