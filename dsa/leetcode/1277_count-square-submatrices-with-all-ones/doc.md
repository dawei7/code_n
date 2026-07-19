# Count Square Submatrices with All Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1277 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) |

## Problem Description

### Goal

Given a rectangular binary matrix, count all square submatrices whose cells are entirely `1`. Squares of every possible side length contribute separately, and overlapping squares are each counted at their own position.

For example, an all-ones $2 \times 2$ region contributes its four individual cells as side-one squares and the whole region as one side-two square. Return the total across the complete matrix.

### Function Contract

**Inputs**

- `matrix`: an $m \times n$ matrix whose entries are either `0` or `1`, where $1 \le m,n \le 300$.

**Return value**

- Return the number of axis-aligned square submatrices containing only `1` values.

### Examples

**Example 1**

- Input: `matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]`
- Output: `15`

**Example 2**

- Input: `matrix = [[1,0,1],[1,1,0],[1,1,0]]`
- Output: `7`

**Example 3**

- Input: `matrix = [[1]]`
- Output: `1`
