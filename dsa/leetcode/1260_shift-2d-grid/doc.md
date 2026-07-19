# Shift 2D Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1260 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shift-2d-grid/) |

## Problem Description

### Goal

You are given an $m \times n$ integer `grid`. One shift moves every element one position forward in row-major order: a cell moves to the next column, the final cell of a row moves to the first column of the following row, and the bottom-right cell wraps to the top-left cell.

Apply this operation `k` times and return the resulting two-dimensional grid with the same dimensions. Values are moved rather than changed, and shifts wrap around the complete matrix rather than wrapping independently within each row.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ integer matrix, where $1 \le m,n \le 50$.
- `k`: the number of shifts, with $0 \le k \le 100$.
- Let $N=mn$ be the number of grid cells.

**Return value**

- Return the matrix after `k` cyclic row-major shifts.

### Examples

**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
- Output: `[[9,1,2],[3,4,5],[6,7,8]]`

**Example 2**

- Input: `grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]`, `k = 4`
- Output: `[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 9`
- Output: `[[1,2,3],[4,5,6],[7,8,9]]`
