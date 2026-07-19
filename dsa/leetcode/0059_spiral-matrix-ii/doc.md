# Spiral Matrix II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 59 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/spiral-matrix-ii/) |

## Problem Description
### Goal
Given a positive integer `n`, create an $n \times n$ square matrix. Place the integers from `1` through $n^{2}$ in increasing order while following a clockwise spiral that begins at the top-left cell.

Move right across the current top edge, down, left, and then up before continuing into the next inner layer. Return the completed matrix with every number used exactly once. For $n = 1$, the matrix contains only `1`.

### Function Contract
**Inputs**

- `n`: the positive side length of the square matrix

**Return value**

The generated `List[List[int]]`.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `[[1,2,3],[8,9,4],[7,6,5]]`

**Example 2**

- Input: `n = 1`
- Output: `[[1]]`

**Example 3**

- Input: `n = 2`
- Output: `[[1,2],[4,3]]`
