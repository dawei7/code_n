# Set Matrix Zeroes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 73 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) |

## Problem Description
### Goal
You are given a nonempty rectangular integer matrix. For every cell whose original value is zero, set every entry in that cell's row and every entry in its column to zero.

All changes are determined by the initially zero cells; a zero created during the transformation must not trigger additional rows or columns. The native method modifies the matrix in place and returns nothing. The cOde(n) adapter returns that same mutated object so the completed grid can be checked directly.

### Function Contract
**Inputs**

- `matrix`: a nonempty rectangular `List[List[int]]`

**Return value**

The mutated matrix in the app adapter; LeetCode's `setZeroes` method returns nothing.

### Examples
**Example 1**

- Input: `matrix = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `[[1,0,1],[0,0,0],[1,0,1]]`

**Example 2**

- Input: `matrix = [[0,1],[1,1]]`
- Output: `[[0,0],[0,1]]`

**Example 3**

- Input: `matrix = [[1,2],[3,4]]`
- Output: `[[1,2],[3,4]]`
