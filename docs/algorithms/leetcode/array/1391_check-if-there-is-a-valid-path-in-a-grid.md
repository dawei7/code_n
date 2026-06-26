# Check if There is a Valid Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1391 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [check-if-there-is-a-valid-path-in-a-grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) |

## Problem Description & Examples
### Goal
Each cell contains a street shape connecting two directions. Starting at the top-left cell, decide whether the street connections allow travel to the bottom-right cell without crossing an incompatible edge.

### Function Contract
**Inputs**

- `grid`: an `m x n` matrix of street type ids from `1` to `6`.

**Return value**

`true` if there is a connected valid path from `(0, 0)` to `(m - 1, n - 1)`, otherwise `false`.

### Examples
**Example 1**

- Input: `grid = [[2,4,3],[6,5,2]]`
- Output: `true`

**Example 2**

- Input: `grid = [[1,2,1],[1,2,1]]`
- Output: `false`

**Example 3**

- Input: `grid = [[1,1,2]]`
- Output: `false`

---

## Underlying Base Algorithm(s)
Graph traversal with compatibility checks. Map each street type to its open directions, move only along open exits, and require the neighboring street to have the opposite opening.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)` for visited state or traversal queue/stack.
