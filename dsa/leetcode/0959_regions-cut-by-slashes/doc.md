# Regions Cut By Slashes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 959 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [regions-cut-by-slashes](https://leetcode.com/problems/regions-cut-by-slashes/) |

## Problem Description

### Goal

An $N\times N$ grid is made of unit squares. Every square contains either a forward slash `/`, a backslash `\`, or a blank space. A slash divides its square diagonally, while a blank leaves the square undivided.

The drawn segments and the outer boundary partition the grid into contiguous regions. Given the rows as `grid`, count all resulting regions. In serialized string data a backslash is escaped, but it represents one diagonal character in the corresponding square.

### Function Contract

**Inputs**

- `grid`: an $N\times N$ list of strings, where $1 \le N \le 30$.
- Every character is `/`, `\`, or a space.

**Return value**

Return the number of connected regions created by the diagonals and blank squares.

### Examples

**Example 1**

- Input: `grid = [" /","/ "]`
- Output: `2`

**Example 2**

- Input: `grid = [" /","  "]`
- Output: `1`

**Example 3**

- Input: `grid = ["/\\","\\/"]`
- Output: `5`
