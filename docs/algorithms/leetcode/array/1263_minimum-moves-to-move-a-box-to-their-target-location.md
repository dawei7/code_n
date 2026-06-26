# Minimum Moves to Move a Box to Their Target Location

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1263 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Heap (Priority Queue), Matrix |
| Official Link | [minimum-moves-to-move-a-box-to-their-target-location](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/) |

## Problem Description & Examples
### Goal
In a grid with walls, one player, one box, and one target, find the minimum number of box pushes needed to move the box onto the target.

### Function Contract
**Inputs**

- `grid`: matrix containing walls `#`, empty cells `.`, player `S`, box `B`, and target `T`.

**Return value**

The fewest pushes required, or `-1` if the target cannot be reached.

### Examples
**Example 1**

- Input: `grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `3`

**Example 2**

- Input: `grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#","#","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `-1`

**Example 3**

- Input: `grid = [["#","#","#","#","#","#"],["#","T",".",".","#","#"],["#",".","#","B",".","#"],["#",".",".",".",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `5`

---

## Underlying Base Algorithm(s)
Breadth-first search over box/player states with reachability checks.

---

## Complexity Analysis
- **Time Complexity**: `O((m * n)^2)` in the straightforward BFS with player reachability searches.
- **Space Complexity**: `O((m * n)^2)` for visited box/player states.
