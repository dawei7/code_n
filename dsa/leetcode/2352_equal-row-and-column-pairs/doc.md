# Equal Row and Column Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2352 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/equal-row-and-column-pairs/) |

## Problem Description

### Goal

Given a 0-indexed square integer matrix `grid` with $n$ rows and $n$ columns,
count the ordered index pairs $(r_i,c_j)$ for which row $r_i$ and column $c_j$
contain exactly the same sequence of values. Both the values and their order
must agree at every position.

Every matching row index and column index contributes separately. Consequently,
if the same sequence occurs in several rows or several columns, all
combinations of those occurrences are counted. Return the total number of
equal row-column pairs.

### Function Contract

**Inputs**

- `grid`: An $n \times n$ integer matrix, where $1 \le n \le 200$ and
  $1 \le \texttt{grid[i][j]} \le 10^5$.

**Return value**

The number of ordered row-column index pairs whose value sequences are equal.

### Examples

#### Example 1

- **Input:** `grid = [[3,2,1],[1,7,6],[2,7,7]]`
- **Output:** `1`
- **Explanation:** Row 2 and column 1 both equal `[2,7,7]`.

#### Example 2

- **Input:** `grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]`
- **Output:** `3`
- **Explanation:** Row 0 matches column 0, while rows 2 and 3 each match column 2.

#### Example 3

- **Input:** `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- **Output:** `9`
- **Explanation:** Each of the three rows matches each of the three columns.
