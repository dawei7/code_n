# Minimum Sensors to Cover Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3648 |
| Difficulty | Medium |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-sensors-to-cover-grid/) |

## Problem Description
### Goal

Consider an $n\times m$ grid of cells. A sensor may be placed on any cell. A cell is covered when its Chebyshev distance from at least one sensor is at most `k`, where the distance between $(r_1,c_1)$ and $(r_2,c_2)$ is

$$
\max\left(\lvert r_1-r_2\rvert,\lvert c_1-c_2\rvert\right).
$$

Thus, away from grid boundaries, one sensor covers a square with side length $2k+1$. Return the minimum number of sensors whose combined coverage contains every grid cell.

### Function Contract
**Inputs**

- `n`: The number of rows, with $1\le n\le 1000$.
- `m`: The number of columns, with $1\le m\le 1000$.
- `k`: The non-negative Chebyshev coverage radius, with $0\le k\le 1000$.

**Return value**

Return the minimum number of sensors needed to cover the entire grid.

### Examples
**Example 1**

- Input: `n = 5`, `m = 5`, `k = 1`
- Output: `4`
- Explanation: Each sensor spans at most three rows and three columns, so two bands are required in each dimension.

**Example 2**

- Input: `n = 2`, `m = 2`, `k = 2`
- Output: `1`
- Explanation: One sensor's radius reaches every cell of the grid.
