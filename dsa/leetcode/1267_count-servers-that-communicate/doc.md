# Count Servers that Communicate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1267 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-servers-that-communicate/) |

## Problem Description

### Goal

A server center is represented by an $m \times n$ integer matrix `grid`. A cell containing `1` holds a server, while a cell containing `0` is empty.

Two servers can communicate when they occupy the same row or the same column; no requirement is imposed on the cells between them. Count the servers that can communicate with at least one other server. Each qualifying server contributes once even if it shares both a row and a column with other servers.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ binary matrix, where $1 \le m,n \le 250$.

Let $V=mn$ be the number of cells in the server-center map.

**Return value**

- Return the number of cells containing a server that shares its row or column with another server.

### Examples

**Example 1**

- Input: `grid = [[1,0],[0,1]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,0],[1,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]`
- Output: `4`
