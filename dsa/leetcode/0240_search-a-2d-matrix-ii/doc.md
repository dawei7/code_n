# Search a 2D Matrix II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 240 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/) |

## Problem Description
### Goal
Given a rectangular integer matrix, every row is sorted from left to right in ascending order and every column is sorted from top to bottom in ascending order. Determine whether any cell contains the integer `target`.

Return `True` when at least one occurrence exists and `False` otherwise. Duplicate matrix values are allowed, and only one match is needed. Use both sorting directions to avoid an exhaustive scan under the required complexity. The target may lie outside the matrix's total value range, and an empty matrix representation contains no matching cell.

### Function Contract
**Inputs**

- `matrix`: a rectangular integer matrix sorted left-to-right and top-to-bottom
- `target`: the integer to locate

**Return value**

`True` if any matrix cell equals `target`; otherwise `False`.

### Examples
**Example 1**

- Input: `matrix = [[1,4,7],[2,5,8],[3,6,9]], target = 5`
- Output: `True`

**Example 2**

- Input: `matrix = [[1,4,7],[2,5,8],[3,6,9]], target = 10`
- Output: `False`

**Example 3**

- Input: `matrix = [[-5]], target = -5`
- Output: `True`
