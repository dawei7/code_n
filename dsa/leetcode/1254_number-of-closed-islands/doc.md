# Number of Closed Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1254 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-closed-islands/) |

## Problem Description

### Goal

You are given a rectangular binary `grid` in which `0` represents land and `1` represents water. An island is a maximal group of land cells connected horizontally or vertically; diagonal contact does not connect two land cells.

A closed island is an island completely surrounded by water, which means none of its land cells can reach the outer boundary of the grid through other land cells. Return the number of closed islands. The input dimensions are at least large enough to contain an interior region.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ matrix containing only `0` and `1`, where $1 \le m,n \le 100$.
- Let $N=mn$ be the total number of cells.

**Return value**

- Return the number of four-directionally connected land components that do not touch the grid boundary.

### Examples

**Example 1**

- Input: `grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `1`
