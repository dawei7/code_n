# Number of Enclaves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1020 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union Find, Matrix |
| Official Link | [number-of-enclaves](https://leetcode.com/problems/number-of-enclaves/) |

## Problem Description & Examples
### Goal
Given a binary grid where `1` means land and `0` means water, count land cells that cannot reach the grid boundary by moving up, down, left, or right through land.

### Function Contract
**Inputs**

- `grid`: List[List[int]]

**Return value**

int - number of enclosed land cells

### Examples
**Example 1**

- Input: `grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]`
- Output: `3`

**Example 2**

- Input: `grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Boundary flood fill.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` worst-case recursion/stack space
