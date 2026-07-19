# Cyclically Rotating a Grid

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/cyclically-rotating-a-grid/) |
| Frontend ID | 1914 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an $R\times C$ integer matrix in which both dimensions are even. Its cells form nested rectangular layers: the outer border is the first layer, the border remaining after removing it is the next layer, and so on.

One cyclic rotation moves every element of every layer to its adjacent position in the counter-clockwise direction. Apply this operation exactly `k` times to all layers and return the resulting matrix. Layers rotate independently, and their different perimeter lengths mean the same `k` can produce different effective shifts.

### Function Contract

**Inputs**

- `grid`: an $R\times C$ matrix of integers.
- `k`: the positive number of counter-clockwise rotations.
- $2 \le R,C \le 50$, and both $R$ and $C$ are even.
- $1 \le \texttt{grid[row][column]} \le 5000$.
- $1 \le k \le 10^9$.

**Return value**

- Return the matrix after every layer has been rotated counter-clockwise by `k` positions.

### Examples

**Example 1**

- Input: `grid = [[40,10],[30,20]], k = 1`
- Output: `[[10,20],[40,30]]`

Each corner value moves to the next corner in the counter-clockwise direction.

**Example 2**

- Input: `grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2`
- Output: `[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]`

The outer and inner layers each advance two positions along their own perimeter.

**Example 3**

- Input: `grid = [[1,2,3,4],[5,6,7,8]], k = 1`
- Output: `[[2,3,4,8],[1,5,6,7]]`

The single rectangular layer has perimeter eight.
