# Check if There is a Valid Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1391 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) |

## Problem Description

### Goal

An $m \times n$ grid represents streets. Every cell contains one of six street types, and each type joins exactly two sides of its cell: type `1` joins left and right, type `2` joins up and down, type `3` joins left and down, type `4` joins right and down, type `5` joins left and up, and type `6` joins right and up.

A move between orthogonally adjacent cells is valid only when the current street opens toward the neighbor and the neighboring street opens back toward the current cell. Street pieces cannot be changed or rotated.

Determine whether the existing streets contain a valid path from the upper-left cell `(0, 0)` to the lower-right cell `(m - 1, n - 1)`.

### Function Contract

**Inputs**

- `grid`: a nonempty $m \times n$ matrix whose entries are street types from `1` through `6`, with $1 \le m,n \le 300$.

**Return value**

- `true` if compatible street connections join the upper-left and lower-right cells; otherwise `false`.

### Examples

**Example 1**

- Input: `grid = [[2,4,3],[6,5,2]]`
- Output: `true`

**Example 2**

- Input: `grid = [[1,2,1],[1,2,1]]`
- Output: `false`

**Example 3**

- Input: `grid = [[1,1,2]]`
- Output: `false`
