# Kth Largest Element in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 215 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) |

## Problem Description
### Goal
Given a nonempty integer array and a valid one-based rank `k`, identify the element that would occupy position `k` if all array occurrences were arranged from largest to smallest. The rank is based on positions in that ordering, not on distinct values.

Return the value at that rank. Duplicate occurrences therefore occupy separate positions and can cause the same value to represent several ranks. For example, $k = 1$ requests a maximum, while `k` equal to the array length requests a minimum. The function returns only the element value and need not return a sorted array or its original index.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list
- `k`: a one-based rank from the largest end

**Return value**

The value at that rank.

### Examples
**Example 1**

- Input: `[3,2,1,5,6,4], k = 2`
- Output: `5`

**Example 2**

- Input: `[3,2,3,1,2,4,5,5,6], k = 4`
- Output: `4`

**Example 3**

- Input: `[7], k = 1`
- Output: `7`
