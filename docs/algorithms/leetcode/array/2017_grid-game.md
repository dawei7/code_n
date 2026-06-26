# Grid Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2017 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [grid-game](https://leetcode.com/problems/grid-game/) |

## Problem Description & Examples
### Goal
Two robots move from the top-left to bottom-right of a `2 x n` grid, each moving only right or down. The first robot zeros its path; minimize the maximum score the second robot can then collect.

### Function Contract
**Inputs**

- `grid`: a `2 x n` matrix of points.

**Return value**

Return the minimum possible score of the second robot assuming both play optimally.

### Examples
**Example 1**

- Input: `grid = [[2,5,4],[1,5,1]]`
- Output: `4`

**Example 2**

- Input: `grid = [[3,3,1],[8,5,2]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1,3,1,15],[1,3,3,1]]`
- Output: `7`

---

## Underlying Base Algorithm(s)
The first robot chooses the column where it drops to the bottom row. After that, the second robot can only collect either the remaining top-row suffix or bottom-row prefix. Scan drop columns using prefix/suffix sums and minimize the larger of those two quantities.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
