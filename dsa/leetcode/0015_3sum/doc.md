# 3Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 15 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/3sum/) |

## Problem Description
### Goal
Given an integer array `nums`, choose three different indices whose values sum to zero. Find every distinct triplet of values that can be formed this way; the same array position cannot supply more than one member of a triplet.

Return the complete collection of zero-sum triplets. Two results containing the same three values in a different order are the same triplet and must appear only once, even when duplicate input values allow many index choices. The triplets and the values within them may be returned in any order.

### Function Contract
**Inputs**

- `nums`: `List[int]`

**Return value**

A `List[List[int]]` containing all unique zero-sum triplets.

### Examples
**Example 1**

- Input: `nums = [-1, 0, 1, 2, -1, -4]`
- Output: `[[-1, -1, 2], [-1, 0, 1]]`

**Example 2**

- Input: `nums = [0, 1, 1]`
- Output: `[]`

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `[[0, 0, 0]]`
