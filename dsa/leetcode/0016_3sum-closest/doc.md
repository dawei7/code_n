# 3Sum Closest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 16 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/3sum-closest/) |

## Problem Description
### Goal
You are given an integer array `nums` containing at least three values and an integer `target`. Choose three distinct array positions and add their values. Among all such triples, seek the sum whose absolute difference from the target is smallest.

Return that three-value sum, not the indices or the distance from the target. Duplicate values may participate when they occupy different positions. Every input is guaranteed to have exactly one closest sum, so no tie-breaking behavior is required.

### Function Contract
**Inputs**

- `nums`: `List[int]` containing at least three values
- `target`: `int`

**Return value**

An `int` containing the uniquely closest three-value sum.

### Examples
**Example 1**

- Input: `nums = [-1, 2, 1, -4], target = 1`
- Output: `2`

**Example 2**

- Input: `nums = [0, 0, 0], target = 1`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1, 0], target = -100`
- Output: `2`
