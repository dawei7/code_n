# Sum of Remoteness of All Cells

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2852 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-remoteness-of-all-cells/) |

## Problem Description

### Goal

You are given a 0-indexed square matrix `grid` of order $n \times n$. Every cell either contains a positive integer or the value `-1`, which marks that cell as blocked. From a nonblocked cell, movement is allowed to another nonblocked cell only when the two cells share an edge.

For a nonblocked cell `(i, j)`, its remoteness $R[i][j]$ is the sum of the positive values in every nonblocked cell `(x, y)` from which `(i, j)` cannot be reached. Reachability is symmetric under the allowed movements. A blocked cell has remoteness `0`.

Return the sum of $R[i][j]$ over every cell in the matrix.

### Function Contract

**Inputs**

- `grid`: An $n \times n$ integer matrix, where each entry is `-1` or an integer from $1$ through $10^6$.

The matrix order satisfies $1 \le n \le 300$.

**Return value**

- The total remoteness of all cells, including zero contribution from blocked cells.

### Examples

#### Example 1

- **Input:** `grid = [[-1,1,-1],[5,-1,4],[-1,3,-1]]`
- **Output:** `39`
- **Explanation:** All four positive cells are isolated. Their remoteness values are `12`, `8`, `9`, and `10`, whose sum is `39`.

#### Example 2

- **Input:** `grid = [[-1,3,4],[-1,-1,-1],[3,-1,-1]]`
- **Output:** `13`
- **Explanation:** The adjacent values `3` and `4` form one component, while the lower `3` is isolated. The two upper cells each contribute `3`, and the lower cell contributes `7`.

#### Example 3

- **Input:** `grid = [[1]]`
- **Output:** `0`
- **Explanation:** The only nonblocked cell has no unreachable positive cell.
