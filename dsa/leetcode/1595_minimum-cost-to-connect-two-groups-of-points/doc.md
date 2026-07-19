# Minimum Cost to Connect Two Groups of Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1595 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/) |

## Problem Description
### Goal
There are two groups of points. The first contains $m$ points and the second contains $n$ points, with $m \ge n$. Matrix `cost` has $m$ rows and $n$ columns, and `cost[i][j]` is the price of adding a connection between point $i$ in the first group and point $j$ in the second group.

Choose any set of connections such that every point in both groups is incident to at least one chosen connection. A point may be connected to several points in the opposite group; there is no one-to-one restriction. Return the minimum possible sum of the selected connection costs.

### Function Contract
**Inputs**

- `cost`: an $m \times n$ integer matrix where $1 \le n \le m \le 12$ and $0 \le \texttt{cost[i][j]} \le 100$.

**Return value**

Return the minimum total cost of connections that cover every point in both groups.

### Examples
**Example 1**

- Input: `cost = [[15, 96], [36, 2]]`
- Output: `17`

**Example 2**

- Input: `cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]`
- Output: `4`
- Explanation: The middle point of the first group may connect to two points in the second group; multiple connections per point are allowed.

**Example 3**

- Input: `cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]`
- Output: `10`
