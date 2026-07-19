# Grid Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2017 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/grid-game/) |

## Problem Description

### Goal

Two robots traverse a $2\times N$ grid from the top-left cell to the
bottom-right cell. A move goes only right or down, so each path changes from
the top row to the bottom row exactly once.

The first robot moves first, collects its path's points, and replaces every
visited cell with zero. The second robot then chooses a path through the
modified grid. The first robot minimizes the second robot's score, while the
second maximizes it. Return the score produced when both choose optimally;
their paths may intersect on cells that have become zero.

### Function Contract

**Inputs**

- `grid`: exactly two rows of $N$ integers, where
  $1\le N\le5\cdot10^4$ and $1\le\texttt{grid[r][c]}\le10^5$.

**Return value**

Return the minimum score the first robot can force against an optimal second
robot.

### Examples

**Example 1**

- Input: `grid = [[2, 5, 4], [1, 5, 1]]`
- Output: `4`

**Example 2**

- Input: `grid = [[3, 3, 1], [8, 5, 2]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1, 3, 1, 15], [1, 3, 3, 1]]`
- Output: `7`
