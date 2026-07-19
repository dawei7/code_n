# 4Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 18 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/4sum/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `target`, choose four different array indices whose values add exactly to the target. Find all distinct quadruplets of values obtainable from valid index selections.

Return all unique quadruplets in any order. Different index choices that yield the same four values, or a different ordering of those values, do not create another result; duplicated input values may still be used when enough separate occurrences exist.

### Function Contract
**Inputs**

- `nums`: `List[int]`
- `target`: `int`

**Return value**

A `List[List[int]]` containing all unique target-sum quadruplets.

### Examples
**Example 1**

- Input: `nums = [1, 0, -1, 0, -2, 2], target = 0`
- Output: `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`

**Example 2**

- Input: `nums = [2, 2, 2, 2, 2], target = 8`
- Output: `[[2, 2, 2, 2]]`

**Example 3**

- Input: `nums = [1, 2, 3], target = 6`
- Output: `[]`
