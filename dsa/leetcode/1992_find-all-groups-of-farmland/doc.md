# Find All Groups of Farmland

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1992 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-groups-of-farmland/) |

## Problem Description
### Goal
The 0-indexed binary matrix `land` represents a rectangular map. A cell holding
`0` is forest, while `1` is farmland. Every farmland group is a filled,
axis-aligned rectangle. Separate groups never share an edge, although they may
be diagonally near one another.

For each group, report its top-left and bottom-right coordinates as
`[topRow, leftColumn, bottomRow, rightColumn]`. Return all such four-value
descriptions in any order. If the map contains no farmland, return an empty
list.

### Function Contract
**Inputs**

- `land`: an $M \times N$ binary matrix, where $1 \le M, N \le 300$.
- Every four-directionally connected farmland component is guaranteed to be a
  completely filled rectangle, and distinct components are not edge-adjacent.

**Return value**

- One rectangle `[r1, c1, r2, c2]` for every farmland group, using inclusive
  corner coordinates.
- Rectangle order is irrelevant.

### Examples
**Example 1**

- Input: `land = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]`
- Output: `[[0, 0, 0, 0], [1, 1, 2, 2]]`

**Example 2**

- Input: `land = [[1, 1], [1, 1]]`
- Output: `[[0, 0, 1, 1]]`

**Example 3**

- Input: `land = [[0]]`
- Output: `[]`
