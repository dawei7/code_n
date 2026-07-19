# Min Cost to Connect All Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1584 |
| Difficulty | Medium |
| Topics | Array, Union-Find, Graph Theory, Minimum Spanning Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/) |

## Problem Description
### Goal

Given distinct points on a two-dimensional plane, connecting points $i$ and $j$ costs their Manhattan distance:

$$
\lvert x_i-x_j\rvert+\lvert y_i-y_j\rvert.
$$

Choose connections so that every point is reachable from every other point and there is exactly one simple path between each pair. Thus, the chosen connections form a spanning tree over the points.

Return the minimum possible sum of connection costs. Any pair of points may be connected directly; only the total tree cost is returned.

### Function Contract
**Inputs**

- `points`: An array of $N$ distinct coordinate pairs `[x, y]`, where $1 \le N \le 1000$ and $-10^6 \le x,y \le 10^6$.

**Return value**

Return the minimum total Manhattan-distance cost of a tree connecting every point.

### Examples
**Example 1**

- Input: `points = [[0,0],[2,2],[3,10],[5,2],[7,0]]`
- Output: `20`

**Example 2**

- Input: `points = [[3,12],[-2,5],[-4,1]]`
- Output: `18`

**Example 3**

- Input: `points = [[0,0]]`
- Output: `0`
