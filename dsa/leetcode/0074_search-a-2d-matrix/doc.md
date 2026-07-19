# Search a 2D Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 74 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/) |

## Problem Description
### Goal
You are given a nonempty rectangular integer matrix with a global sorted structure. Each row is sorted in non-decreasing order, and the first integer of every row is greater than the final integer of the preceding row.

Determine whether `target` occurs in any cell and return a boolean. In row-major order, the matrix behaves like one sorted array, so the intended search should exploit that ordering rather than inspect every cell. A one-cell matrix follows the same contract.

### Function Contract
**Inputs**

- `matrix`: a nonempty `m` by `n` integer matrix with global row-major ordering
- `target`: the integer to find

**Return value**

`True` if the matrix contains `target`, otherwise `False`.

### Examples
**Example 1**

- Input: `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3`
- Output: `True`

**Example 2**

- Input: the same matrix, `target = 13`
- Output: `False`

**Example 3**

- Input: `matrix = [[1]], target = 1`
- Output: `True`
