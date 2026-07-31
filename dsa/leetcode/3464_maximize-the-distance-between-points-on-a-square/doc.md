# Maximize the Distance Between Points on a Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3464 |
| Difficulty | Hard |
| Topics | Array, Math, Binary Search, Geometry, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/) |

## Problem Description
### Goal
Consider the axis-aligned square whose corners are $(0,0)$, $(0,\texttt{side})$, $(\texttt{side},0)$, and $(\texttt{side},\texttt{side})$. Every coordinate in `points` is a distinct location on this square's boundary. Select exactly `k` of the supplied points; points on the boundary that are absent from the input cannot be chosen.

For a selected pair $(x_i,y_i)$ and $(x_j,y_j)$, its Manhattan distance is $\lvert x_i-x_j\rvert+\lvert y_i-y_j\rvert$. Each selection has a score equal to the smallest such distance among all pairs of its chosen points. Return the largest score attainable by any valid selection of `k` points.

### Function Contract
**Inputs**

- `side`: The positive integer side length of the square.
- `points`: A list of distinct integer coordinate pairs `[x, y]`, each lying on the square's boundary.
- `k`: The number of points that must be selected.

Let $n=\lvert\texttt{points}\rvert$. The constraints are $1\le\texttt{side}\le10^9$, $4\le n\le\min(4\cdot\texttt{side},15000)$, and $4\le k\le\min(25,n)$.

**Return value**

Return the maximum possible minimum Manhattan distance among the `k` selected points.

### Examples
**Example 1**

- Input: `side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4`
- Output: `2`

All four corners must be selected, and each neighboring corner is distance $2$ from the next.

**Example 2**

- Input: `side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4`
- Output: `1`

One optimal selection is `(0,0)`, `(2,0)`, `(2,2)`, and `(2,1)`.

**Example 3**

- Input: `side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5`
- Output: `1`

Five boundary points can be selected with every pair at least distance $1$ apart, but distance $2$ is impossible.
