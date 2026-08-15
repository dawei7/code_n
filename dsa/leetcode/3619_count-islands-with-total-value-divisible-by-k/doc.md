# Count Islands With Total Value Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3619 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/) |

## Problem Description

### Goal

The matrix `grid` contains nonnegative integers. A positive cell represents land, while a zero cell represents water. An island is a maximal group of positive cells connected horizontally or vertically; diagonal contact does not connect two cells.

For each island, add the values of all its cells to obtain that island's total value. Count and return the islands whose total is divisible by the positive integer `k`. Water cells never contribute to a total, and distinct islands are evaluated independently.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix of nonnegative cell values.
- `k`: The positive divisor used to test each island total.

The matrix dimensions satisfy $1 \le m,n \le 1000$ and $1 \le mn \le 10^5$. Cell values lie from 0 through $10^6$, and $1 \le k \le 10^6$.

**Return value**

Return the number of four-directionally connected positive-cell islands whose cell-value sum is divisible by `k`.

### Examples

#### Example 1

- **Input:** `grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5`
- **Output:** `2`
- **Explanation:** Four islands exist, and two of their totals are multiples of 5.

#### Example 2

- **Input:** `grid = [[3,0,3,0],[0,3,0,3],[3,0,3,0]], k = 3`
- **Output:** `6`
- **Explanation:** The six positive cells are diagonally separated one-cell islands, each totaling 3.

#### Example 3

- **Input:** `grid = [[1, 2], [3, 4]], k = 5`
- **Output:** `1`
- **Explanation:** All four cells form one island with total 10.
