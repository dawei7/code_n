# Minimize Maximum Value in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2371 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Union-Find, Graph Theory, Topological Sort, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-maximum-value-in-a-grid/) |

## Problem Description

### Goal

Given an $m \times n$ matrix `grid` whose entries are distinct positive integers, replace every entry with a positive integer. Within each individual row and each individual column, the replacement values must preserve every strict comparison from the original matrix.

Among all matrices that preserve those relative orders, minimize the largest replacement value and return one resulting matrix. Multiple optimal matrices may exist, and any one of them is acceptable. Comparisons between cells that share neither a row nor a column impose no ordering requirement.

### Function Contract

**Inputs**

- `grid`: An $m \times n$ matrix of distinct integers, where $1 \le m,n \le 1000$, $1 \le mn \le 10^5$, and $1 \le \texttt{grid[i][j]} \le 10^9$.

Let $N = mn$ denote the number of cells.

**Return value**

- Return an $m \times n$ positive-integer matrix that preserves all within-row and within-column relative orders while attaining the smallest possible maximum value.

**Order preservation**

- If two original cells share a row or column and one value is larger, its replacement must also be strictly larger.
- Cells without a shared row or column do not constrain one another and may receive equal replacement values.

### Examples

**Example 1**

- Input: `grid = [[3,1],[2,5]]`
- Output: `[[2,1],[1,2]]`
- Explanation: Both row orders and both column orders are preserved, and no valid replacement can have a maximum below $2$.

**Example 2**

- Input: `grid = [[10]]`
- Output: `[[1]]`
- Explanation: The only cell can receive the smallest positive integer.
