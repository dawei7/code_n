# Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1284 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/) |

## Problem Description
### Goal
You are given an $m \times n$ binary matrix. In one step, choose a cell and flip its value: zero becomes one and one becomes zero. The same step also flips every existing orthogonal neighbor of the chosen cell—those directly above, below, left, or right. Diagonal cells are not neighbors, and cells beyond a matrix boundary are ignored.

Find the minimum number of steps that converts the entire matrix to a zero matrix. If no sequence of allowed flips can make every cell zero, return `-1`.

### Function Contract
**Inputs**

- `mat`: an $m \times n$ matrix containing only zeroes and ones, where $1 \le m,n \le 3$.
- Let $k = mn$ be the number of cells.

**Return value**

The fewest cell-flip steps needed to reach the all-zero matrix, or `-1` when the zero matrix is unreachable.

### Examples
**Example 1**

- Input: `mat = [[0,0],[0,1]]`
- Output: `3`

**Example 2**

- Input: `mat = [[0]]`
- Output: `0`
- Explanation: No step is needed because the input is already a zero matrix.

**Example 3**

- Input: `mat = [[1,0,0],[1,0,0]]`
- Output: `-1`
- Explanation: No combination of legal flips reaches the zero matrix.
