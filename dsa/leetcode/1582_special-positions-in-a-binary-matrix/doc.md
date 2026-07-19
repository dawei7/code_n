# Special Positions in a Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1582 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/special-positions-in-a-binary-matrix/) |

## Problem Description
### Goal

Given an $R \times C$ binary matrix `mat`, call position $(i,j)$ special when `mat[i][j]` is $1$ and every other entry in row $i$ and column $j$ is $0$.

The row and column conditions both matter: a lone $1$ within its row is not special if another row contains a $1$ in the same column, and a column-unique $1$ is not special when its row contains another $1$.

Count and return all special positions in the matrix. Each qualifying $1$ contributes exactly once.

### Function Contract
**Inputs**

- `mat`: A rectangular binary matrix with $R$ rows and $C$ columns, where $1 \le R,C \le 100$.

**Return value**

Return the number of positions whose value is $1$ and whose row and column each contain exactly one $1$.

### Examples
**Example 1**

- Input: `mat = [[1,0,0],[0,0,1],[1,0,0]]`
- Output: `1`

**Example 2**

- Input: `mat = [[1,0,0],[0,1,0],[0,0,1]]`
- Output: `3`

**Example 3**

- Input: `mat = [[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]`
- Output: `2`
