# Minimum Cost Path with Alternating Directions II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3603 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/) |

## Problem Description

### Goal

Consider an `m`-by-`n` grid with zero-indexed cells. Entering `(i, j)` costs $(i+1)(j+1)$, and `waitCost[i][j]` is the separate cost of spending one required waiting second on that cell. Begin by entering `(0, 0)` and paying its entrance cost of $1$.

Actions then alternate by second. On every odd-numbered second, move exactly one cell right or down and pay the destination cell's entrance cost. On every even-numbered second, remain on the current cell for exactly one second and pay that cell's waiting cost. All movement stays inside the grid.

Reach `(m - 1, n - 1)` with the minimum total cost. The journey ends immediately upon entering the destination, so no waiting cost is paid there; likewise, the first action after the initial entry is a move, so no waiting cost is paid at the starting cell.

### Function Contract

**Inputs**

- `m`: the number of grid rows
- `n`: the number of grid columns
- `waitCost`: an `m`-by-`n` matrix of nonnegative waiting costs

The dimensions satisfy $1 \le m,n \le 10^5$ and $2 \le mn \le 10^5$. Every waiting cost is at most $10^5$.

**Return value**

The minimum total entrance and required waiting cost for a valid path from the top-left cell to the bottom-right cell.

### Examples

#### Example 1

- **Input:** `m = 1, n = 2, waitCost = [[1,2]]`
- **Output:** `3`

Pay `1` to enter the start, then move right and pay entrance cost `2`. The destination is reached before a wait occurs.

#### Example 2

- **Input:** `m = 2, n = 2, waitCost = [[3,5],[2,4]]`
- **Output:** `9`

Moving down, waiting at `(1, 0)`, and then moving right costs `1 + 2 + 2 + 4 = 9`.

#### Example 3

- **Input:** `m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]]`
- **Output:** `16`

An optimal route goes right, waits, goes down, waits, and goes right, with total `1 + 2 + 1 + 4 + 2 + 6 = 16`.
