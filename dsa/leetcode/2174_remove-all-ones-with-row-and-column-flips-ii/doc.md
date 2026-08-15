# Remove All Ones With Row and Column Flips II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2174 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/) |

## Problem Description

### Goal

You are given a 0-indexed $m \times n$ binary matrix `grid`. An operation must
select a cell `(i, j)` whose current value is `1`. That operation changes every
cell in row `i` and every cell in column `j` to `0`; cells already equal to
zero remain zero.

Because an operation can only remove ones, each choice changes which later
intersections are still legal to select. Return the minimum number of
operations required to make every cell zero.

### Function Contract

**Inputs**

- `grid`: a rectangular binary matrix with $1 \le m,n \le 15$ and
  $1 \le mn \le 15$.

Every `grid[i][j]` is either `0` or `1`.

**Return value**

Return the minimum number of legal row-and-column clearing operations needed
to remove all ones. Return `0` when the matrix is already all zero.

### Examples

#### Example 1

- **Input:** `grid = [[1,1,1],[1,1,1],[0,1,0]]`
- **Output:** `2`

#### Example 2

- **Input:** `grid = [[0,1,0],[1,0,1],[0,1,0]]`
- **Output:** `2`

#### Example 3

- **Input:** `grid = [[0,0],[0,0]]`
- **Output:** `0`
