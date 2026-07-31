# Stamping the Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2132 |
| Difficulty | Hard |
| Topics | Array, Greedy, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/stamping-the-grid/) |

## Problem Description
### Goal
You are given an $m\times n$ binary grid. A `0` denotes an empty cell and a
`1` denotes an occupied cell. You also have any number of identical
rectangular stamps, each with the specified height and width.

Place stamps without rotating them. Every stamp must lie completely inside the
grid and may cover only empty cells. Different stamps are allowed to overlap.
Determine whether some collection of valid placements covers every empty cell;
occupied cells must remain uncovered.

### Function Contract
**Inputs**

- `grid`: An $m\times n$ binary matrix with
  $1\le m,n\le 10^5$ and $1\le mn\le 2\cdot 10^5$.
- `stampHeight`: The fixed stamp height, between $1$ and $10^5$.
- `stampWidth`: The fixed stamp width, between $1$ and $10^5$.

**Return value**

`true` if valid, possibly overlapping stamps can cover every empty cell;
otherwise `false`.

### Examples
**Example 1**

- Input: `grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]`,
  `stampHeight = 4`, `stampWidth = 3`
- Output: `true`
- Explanation: Two overlapping placements cover the empty three-column strip.

**Example 2**

- Input: `grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]`,
  `stampHeight = 2`, `stampWidth = 2`
- Output: `false`
- Explanation: Some empty cells cannot belong to an in-bounds stamp without
  also covering an occupied diagonal cell.
