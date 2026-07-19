# Search in Rotated Sorted Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 81 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) |

## Problem Description
### Goal
You are given an integer array sorted in non-decreasing order that may have been rotated at an unknown pivot, moving one prefix behind the remaining suffix. Unlike the distinct-value version, this array may contain duplicates, including equal values across the rotation boundary.

Return whether `target` appears at least once. Duplicate boundary and midpoint values can make the sorted half temporarily ambiguous, so logarithmic elimination is not guaranteed for every input. The array is nonempty and may also be effectively unrotated.

### Function Contract
**Inputs**

- `nums`: a nonempty rotated nondecreasing `List[int]` that may contain duplicates
- `target`: the integer to find

**Return value**

`True` if any occurrence exists, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [2,5,6,0,0,1,2], target = 0`
- Output: `True`

**Example 2**

- Input: the same array, `target = 3`
- Output: `False`

**Example 3**

- Input: `nums = [1,0,1,1,1], target = 0`
- Output: `True`
