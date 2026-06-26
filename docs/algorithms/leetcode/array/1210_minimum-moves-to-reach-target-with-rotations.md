# Minimum Moves to Reach Target with Rotations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1210 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Matrix |
| Official Link | [minimum-moves-to-reach-target-with-rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/) |

## Problem Description & Examples
### Goal
Move a two-cell snake from the top-left horizontal position to the bottom-right horizontal target in a square grid with blocked cells. The snake may move right, move down, or rotate when the surrounding `2 x 2` area is clear.

### Function Contract
**Inputs**

- `grid`: an `n x n` matrix where `0` is empty and `1` is blocked.

**Return value**

The minimum number of moves required, or `-1` if the target cannot be reached.

### Examples
**Example 1**

- Input: `grid = [[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]`
- Output: `11`

**Example 2**

- Input: `grid = [[0,0,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,0]]`
- Output: `9`

**Example 3**

- Input: `grid = [[0,0],[0,0]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Breadth-first search over position-and-orientation states.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`
