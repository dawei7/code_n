# Minimum Number of Days to Disconnect Island

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1568 |
| Difficulty | Hard |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Strongly Connected Component |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) |

## Problem Description
### Goal

A binary grid represents land with `1` and water with `0`. Land cells belong to the same island when they are connected through shared horizontal or vertical sides. The grid is considered disconnected when it contains either no island or more than one island.

On each day, you may choose one land cell and change it to water. Return the minimum number of days required to make the grid disconnected. If it is already disconnected, return `0`; changing at most two cells is always sufficient.

### Function Contract
**Inputs**

- `grid`: An $R \times C$ binary matrix, where $1 \le R,C \le 30$. Each entry is `0` or `1`.

**Return value**

Return the minimum number of land cells that must be changed to water until the number of four-directionally connected islands is not exactly one. The answer is always `0`, `1`, or `2`.

### Examples
**Example 1**

- Input: `grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1,1]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1,0,1,0]]`
- Output: `0`
