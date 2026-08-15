# Manhattan Distances of All Arrangements of Pieces

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/) |
| Frontend ID | 3426 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Consider an $m \times n$ rectangular grid and $k$ identical pieces. A valid arrangement places all $k$ pieces into distinct cells, with at most one piece in any cell.

For one arrangement, consider every unordered pair of pieces and compute the Manhattan distance between their cells. For cells $(x_i,y_i)$ and $(x_j,y_j)$, that distance is $\lvert x_i-x_j \rvert+\lvert y_i-y_j \rvert$.

Sum these pair distances over every valid arrangement. Return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `m`: The number of grid rows.
- `n`: The number of grid columns.
- `k`: The number of identical pieces placed in distinct cells.

Let $N=mn$ be the number of cells. The constraints are $1 \le m,n \le 10^5$, $2 \le N \le 10^5$, and $2 \le k \le N$.

**Return value**

Return the total sum modulo $1{,}000{,}000{,}007$.

### Examples

#### Example 1

- **Input:** `m = 2, n = 2, k = 2`
- **Output:** `8`
- **Explanation:** Four adjacent cell pairs contribute distance `1`, and two diagonal pairs contribute distance `2`.

#### Example 2

- **Input:** `m = 1, n = 4, k = 3`
- **Output:** `20`
- **Explanation:** The four arrangements have total pair distances `4`, `6`, `6`, and `4`.
