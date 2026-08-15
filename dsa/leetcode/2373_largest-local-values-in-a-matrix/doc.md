# Largest Local Values in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2373 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-local-values-in-a-matrix/) |

## Problem Description

### Goal

Given an $n \times n$ integer matrix `grid`, consider every contiguous $3 \times 3$ submatrix. Each such window is identified by its top-left position, or equivalently by the input cell at its center.

Construct an $(n-2) \times (n-2)$ matrix `maxLocal`. For every valid output position `(i, j)`, store the largest of the nine input values in the window spanning rows `i` through `i + 2` and columns `j` through `j + 2`. Return the complete generated matrix.

### Function Contract

**Inputs**

- `grid`: An $n \times n$ integer matrix with $3 \le n \le 100$ and $1 \le \texttt{grid[i][j]} \le 100$.

**Return value**

- Return an $(n-2) \times (n-2)$ matrix where `answer[i][j]` is the maximum value in the contiguous $3 \times 3$ input window beginning at `(i, j)`.

**Window semantics**

- Neighboring windows overlap; each output cell is computed independently from its own nine input cells.
- The first window begins at `(0, 0)`, and the last begins at `(n - 3, n - 3)`.

### Examples

#### Example 1

- **Input:** `grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]`
- **Output:** `[[9,9],[8,6]]`
- **Explanation:** Each of the four output values is the maximum of the corresponding overlapping $3 \times 3$ window.

#### Example 2

- **Input:** `grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]`
- **Output:** `[[2,2,2],[2,2,2],[2,2,2]]`
- **Explanation:** The central `2` belongs to every contiguous $3 \times 3$ window.
