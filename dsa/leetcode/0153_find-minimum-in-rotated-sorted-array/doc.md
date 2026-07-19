# Find Minimum in Rotated Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 153 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |

## Problem Description
### Goal
You are given a nonempty array of unique integers that was sorted in ascending order and then rotated some number of positions. A rotation moves a suffix in front of a prefix while preserving the sorted order inside both resulting portions; rotating zero times is also possible.

Return the smallest value in the array. It is the original sorted sequence's first element and, after a nontrivial rotation, lies at the boundary where a larger value wraps to a smaller one. Meet the required logarithmic running time instead of scanning all entries, and return the sole value directly for a one-element array.

### Function Contract
**Inputs**

- `nums`: a rotated ascending list containing distinct integers

**Return value**

The smallest array value.

### Examples
**Example 1**

- Input: `nums = [3,4,5,1,2]`
- Output: `1`

**Example 2**

- Input: `nums = [4,5,6,7,0,1,2]`
- Output: `0`

**Example 3**

- Input: `nums = [11,13,15,17]`
- Output: `11`
