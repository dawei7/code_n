# Twisted Mirror Path Count

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3665 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/twisted-mirror-path-count/) |

## Problem Description

### Goal

A robot starts at the top-left cell of an $m\times n$ binary grid and seeks the bottom-right cell. It normally moves one cell right or one cell down. A zero marks an empty cell, while a one marks a mirror.

When a rightward move attempts to enter a mirror, the mirror redirects the robot downward into the cell below that mirror. When a downward move attempts to enter a mirror, it redirects the robot rightward into the cell beside the mirror. The incoming direction therefore determines the outgoing direction.

A redirected move may immediately encounter another mirror, causing another direction-dependent reflection. This continues until the robot reaches an empty cell or the destination, or a reflected move leaves the grid. Any route that leaves the boundaries is invalid.

Count the distinct valid paths from the top-left to the bottom-right cell. Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ matrix containing only `0` and `1`, where $2\le m,n\le500$.

The start `grid[0][0]` and destination `grid[m - 1][n - 1]` are always empty.

**Return value**

Return the number of valid right/down paths after applying every forced mirror reflection, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `grid = [[0,1,0],[0,0,1],[1,0,0]]`
- **Output:** `5`
- Five routes survive the mirrors and remain inside the grid.

#### Example 2

- **Input:** `grid = [[0,0],[0,0]]`
- **Output:** `2`
- The ordinary right-then-down and down-then-right routes are both valid.

#### Example 3

- **Input:** `grid = [[0,1,1],[1,1,0]]`
- **Output:** `1`
- One reflection chain reaches the destination; the other is redirected outside the bottom boundary.
