# Shortest Path in a Grid with Obstacles Elimination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1293 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) |

## Problem Description
### Goal
You are given an $m \times n$ binary matrix in which zero is an empty cell and one is an obstacle. Starting at the empty upper-left cell, one step moves up, down, left, or right to an in-bounds neighboring cell.

Reach the empty lower-right cell in the minimum number of steps. During the walk you may eliminate at most `k` obstacles, allowing those obstacle cells to be entered. Return `-1` if no walk satisfies the elimination budget.

### Function Contract
**Inputs**

- `grid`: an $m \times n$ binary matrix, where $1 \le m,n \le 40$ and both endpoint cells are zero.
- `k`: an integer satisfying $1 \le k \le mn$.
- Let $S = mn(k+1)$ be the maximum number of position-and-budget states.

**Return value**

The fewest four-direction steps from $(0,0)$ to $(m-1,n-1)$ using at most `k` obstacle eliminations, or `-1` when no such walk exists.

### Examples
**Example 1**

- Input: `grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]`, `k = 1`
- Output: `6`

**Example 2**

- Input: `grid = [[0,1,1],[1,1,1],[1,0,0]]`, `k = 1`
- Output: `-1`

**Example 3**

- Input: `grid = [[0,1],[0,0]]`, `k = 1`
- Output: `2`
