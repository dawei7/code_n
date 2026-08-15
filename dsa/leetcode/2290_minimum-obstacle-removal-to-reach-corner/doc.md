# Minimum Obstacle Removal to Reach Corner

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2290 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/) |

## Problem Description

### Goal

A 0-indexed $m \times n$ binary matrix `grid` describes a rectangular area.
A cell containing `0` is empty, while a cell containing `1` is an obstacle
that may be removed. Movement is allowed between orthogonally adjacent empty
cells: one step up, down, left, or right.

Remove as few obstacles as possible so that a path exists from the upper-left
cell `(0, 0)` to the lower-right cell `(m - 1, n - 1)`. Return that minimum
number. The start and destination are guaranteed to be empty.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular binary matrix whose two corner endpoints contain `0`.

The dimensions satisfy $1 \le m,n \le 10^5$ and
$2 \le mn \le 10^5$.

**Return value**

The minimum number of obstacle cells that must be removed to connect the two
corners by a four-directional path.

### Examples

#### Example 1

- **Input:** `grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]`
- **Output:** `2`

#### Example 2

- **Input:** `grid = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]`
- **Output:** `0`
