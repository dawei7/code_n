# Find Peak Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 162 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-peak-element/) |

## Problem Description
### Goal
Given a nonempty integer array whose adjacent elements are never equal, find a peak element. An element is a peak when it is strictly greater than the values immediately beside it; beyond either end of the array, imagine a value of negative infinity.

Return the index of any valid peak. Several peaks may exist, and the validator accepts any one of their indices rather than requiring a predetermined choice. An endpoint qualifies when it exceeds its only real neighbor, and the sole element of a length-one array is a peak. Meet the required logarithmic running time instead of scanning every position.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list whose adjacent elements are unequal

**Return value**

Any valid peak index. The app validates the peak property rather than requiring one predetermined index.

### Examples
**Example 1**

- Input: `nums = [1,2,3,1]`
- Output: `2`

**Example 2**

- Input: `nums = [1,2,1,3,5,6,4]`
- Output: `1` or `5`

**Example 3**

- Input: `nums = [1]`
- Output: `0`
