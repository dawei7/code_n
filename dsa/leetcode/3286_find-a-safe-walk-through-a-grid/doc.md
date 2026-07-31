# Find a Safe Walk Through a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3286 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/) |

## Problem Description

### Goal

You begin at the upper-left cell of an $m\times n$ binary grid and want to reach the lower-right cell. From a cell, you may move one step up, down, left, or right while remaining inside the grid.

Entering or starting on a cell whose value is `1` reduces your health by one; a `0` cell costs no health. Your health must remain positive throughout the walk, including after entering the destination. Determine whether some walk reaches the destination with at least one health point remaining.

### Function Contract

**Inputs**

- `grid`: A rectangular binary matrix with $m$ rows and $n$ columns.
- `health`: The positive initial health value.

Each dimension is between $1$ and $50$, the grid contains at least two cells, and $1\le\texttt{health}\le m+n$.

**Return value**

Return `true` if a walk from `(0, 0)` to `(m - 1, n - 1)` visits fewer than `health` unsafe cells; otherwise, return `false`.

### Examples

**Example 1**

- Input: `grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1`
- Output: `true`

A route of only zero-valued cells reaches the destination without reducing health.

**Example 2**

- Input: `grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3`
- Output: `false`

Every route requires at least four initial health points to remain positive at the destination.

**Example 3**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5`
- Output: `true`

The starting cell also costs health. Passing through the safe center permits arrival with positive health.
